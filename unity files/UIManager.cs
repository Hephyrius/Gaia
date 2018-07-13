using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class UIManager : MonoBehaviour {

    public EvolutionManager evo;
    public Text pop;
    public Text gen;
    public Text leftList;
    public Text rightList;

    public float speed;
    public Slider slide;

    private void Start()
    {
        speed = 0.005f;
        slide.value = speed;
    }

    public void updateSpeed()
    {
        speed = slide.value;
    }

    // Update is called once per frame
    void Update () {
        pop.text = "Individual: " + evo.currentSnake.ToString();
        gen.text = "Generation: " + evo.generationNumber.ToString();
        setLeft();
        setRight();
    }

    void setLeft()
    {
        for(int i=0; i< (evo.nets.Count/2); i++)
        {
            if(i == 0)
            {
                float fit = evo.nets[i].GetFitness();
                leftList.text = "Snake " + i.ToString() + " : " + fit.ToString();
            }
            else
            {
                float fit = evo.nets[i].GetFitness();
                leftList.text = leftList.text+"\nSnake " + i.ToString() + " : " +  fit.ToString();
            }
        }
    }

    void setRight()
    {
        for (int i = 0; i < evo.nets.Count / 2; i++)
        {
            if (i == 0)
            {
                int j = (evo.nets.Count / 2) + i;
                float fit = evo.nets[j].GetFitness();
                rightList.text = "Snake " + j.ToString() + " : " + fit.ToString();
            }
            else

            {
                int j = (evo.nets.Count / 2) + i;
                float fit = evo.nets[j].GetFitness();
                rightList.text = rightList.text + "\nSnake " + j.ToString() + " : " + fit.ToString();
            }
        }
    }
}
