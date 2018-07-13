using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EvolutionManager : MonoBehaviour {

    public GameObject Snake;

    public bool Training;
    private int populationSize = 20;
    public int generationNumber = 0;
    private int[] layers = new int[] { 25, 10, 10, 4 }; //17 input and 4 output
    public List<NeuralNetwork> nets;
    private bool leftMouseDown = false;
    private List<SnakeScript> SnakeList = null;
    public int currentSnake;
    public Spawner food;
    private float crossoverRate = 0.5f;

    void FixedUpdate()
    {
        if (Training == false)
        {
            if (generationNumber == 0)
            {
                InitSnakeNeuralNetworks();
            }
            else
            {
                sortList();
                wait();
                for (int i = 0; i < populationSize / 2; i++)
                {

                    nets[i + (populationSize / 2)] = new NeuralNetwork(nets[i + (populationSize / 2)]); //too lazy to write a reset neuron matrix values method....so just going to make a deepcopy lol
                    float ind = (populationSize / 8);
                    int index1 = (int)UnityEngine.Random.Range(0f, ind+1);
                    int index2 = (int)UnityEngine.Random.Range(0f, ind+1);
                    nets[i + (populationSize / 2)].CrossoverThreeWeights(crossoverRate, nets[index1], nets[index2]);
                    nets[i + (populationSize / 2)].Mutate();
                  
                }

                
                for (int i = 0; i < populationSize / 2; i++)
                {
                    float rate = UnityEngine.Random.Range(0f, 1f);
                    if (rate > 0.5f)
                    {
                        nets[i].Mutate();
                    }
                }

                    for (int i = 0; i < populationSize; i++)
                {
                    nets[i].SetFitness(0f);
                }


            }


            generationNumber++;

            Training = true;
            //Invoke("Timer", 15f);
            CreateSnakes();
            currentSnake = 0;
        }
        else
        {

            if(SnakeList[currentSnake].gameObject.activeSelf == false)
            {
                SnakeList[currentSnake].gameObject.SetActive(true);
            }

            if (SnakeList[currentSnake].dead == true)
            {
                SnakeList[currentSnake].gameObject.SetActive(false);
                currentSnake = currentSnake + 1;
                if (currentSnake == populationSize)
                {
                    Training = false;
                }
                else
                {
                    SnakeList[currentSnake].gameObject.SetActive(true);
                }
            }
        }

    }


    private void CreateSnakes()
    {
        if (SnakeList != null)
        {
            for (int i = 0; i < SnakeList.Count; i++)
            {
                GameObject.Destroy(SnakeList[i].gameObject);
            }

        }

        SnakeList = new List<SnakeScript>();

        for (int i = 0; i < populationSize; i++)
        {
            SnakeScript snek = ((GameObject)Instantiate(Snake, new Vector3(-1, 0, -2), Snake.transform.rotation)).GetComponent<SnakeScript>();
            snek.net = nets[i];
            snek.gameObject.SetActive(false);
            SnakeList.Add(snek);
        }

    }

    void InitSnakeNeuralNetworks()
    {
        //population must be even, just setting it to 20 incase it's not
        if (populationSize % 2 != 0)
        {
            populationSize = 20;
        }

        nets = new List<NeuralNetwork>();


        for (int i = 0; i < populationSize; i++)
        {
            NeuralNetwork net = new NeuralNetwork(layers);
            net.Mutate();
            nets.Add(net);
        }
    }


    void wait()
    {
        float timer = 0;

        while (timer < 2f)
        {
            timer = timer + Time.fixedDeltaTime;
        }

    }

    //bubble sorting the list
    void sortList()
    {
        for(int i = nets.Count-1; i>=0; i--)
        {
            for(int j=1; j<=i; j++)
            {

                if(nets[j-1].GetFitness() < nets[j].GetFitness())
                {
                    var temp = nets[j - 1];
                    nets[j - 1] = nets[j];
                    nets[j] = temp;
                }
            }
        }
    }

}
