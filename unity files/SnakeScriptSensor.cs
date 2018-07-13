using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class SnakeScriptSensor : MonoBehaviour {

    int size = 3;
    float timer = 0;
    int direction = 0;
    public GameObject segment;
    public GameObject parent;
    public List<GameObject> body = new List<GameObject>();
    public List<Vector2> positions;
    bool ate;
    bool started = true;
    float startTimer;
    public bool dead = false;
    public List<SensorScript> Sensors = new List<SensorScript>();
    public NeuralNetwork net;
    public int score;
    public int secondsLived;

    private void Start()
    {
        parent = new GameObject();

        for (int i = 1; i < size; i++)
        {
            GameObject part = Instantiate(segment);
            Vector2 pos = this.transform.position;
            pos.y = pos.y - (i*0.5f);
            part.transform.position = pos;
            part.transform.parent = parent.transform;
            //part.transform.parent = this.transform;
            body.Add(part);
            positions.Add(pos);

        }
    }


    // Update is called once per frame
    void FixedUpdate () {

        if (started == true)
        {
            startTimer = startTimer + Time.fixedDeltaTime;
            if(startTimer > 0.25f)
            {
                started = false;
            }
        }

        timer = timer + Time.fixedDeltaTime;

        if (timer > 0.02 && dead == false)
        {
            timer = 0;
            secondsLived = secondsLived + 1;
            if(secondsLived > 300)
            {
                Destroy(parent);
                net.AddFitness((score * 1000));
                net.AddFitness(secondsLived);
                dead = true;
            }
            //get the inputs used by the neural net
            float[] inputs = new float[25];
            for (int i = 0; i < Sensors.Count; i++)
            {
                inputs[i] = Sensors[i].distanceBody;
            }
            for (int i = 0; i < Sensors.Count; i++)
            {
                inputs[Sensors.Count + i] = Sensors[i].distanceWall;
            }
            for (int i = 0; i < Sensors.Count; i++)
            {
                inputs[(Sensors.Count*2) + i] = Sensors[i].distanceFood;
            }
            inputs[24] = direction;

            //make prediction
            float[] output = net.FeedForward(inputs);

            //handle the prediction to control the snake
            int nextDirection = 0;
            if(output[0]> output[1] && output[0]> output[2] && output[0]> output[3])
            {
                nextDirection = 0;
            }
            else if (output[1] > output[0] && output[1] > output[2] && output[1] > output[3])
            {
                nextDirection = 1;
            }
            else if (output[2] > output[0] && output[2] > output[1] && output[2] > output[3])
            {
                nextDirection = 2;
            }
            else if (output[3] > output[0] && output[3] > output[1] && output[3] > output[2])
            {
                nextDirection = 3;
            }

            //logic that prevents illegal logic
            if(direction == 0 && nextDirection == 1)
            {
                nextDirection = 0;
            }
            else if (direction == 1 && nextDirection == 0)
            {
                nextDirection = 1;
            }
            else if (direction == 2 && nextDirection == 3)
            {
                nextDirection = 2;
            }
            else if (direction == 3 && nextDirection == 2)
            {
                nextDirection = 3;
            }


            Vector2 current = new Vector2(this.transform.position.x, this.transform.position.y);


            for (int i = 0; i < body.Count; i++)
            {
                if (i == 0)
                {
                    body[i].transform.position = this.transform.position;
                }
                else
                {
                    body[i].transform.position = positions[i - 1];
                }
            }

            if (ate == true)
            {
                GameObject part = Instantiate(segment);
                Vector2 pos = positions[body.Count - 1];
                part.transform.parent = parent.transform;
                part.transform.position = pos;
                //part.transform.parent = this.transform;
                body.Add(part);
                positions.Add(pos);
                size = size + 1;
                ate = false;
            }

            for (int i = 0; i < body.Count; i++)
            {
                positions[i] = body[i].transform.position;
            }

            if (nextDirection == 0)
            {
                Vector2 pos = this.transform.position;
                pos.y = pos.y + 0.5f;
                this.transform.eulerAngles = new Vector3(0, 0, 0);
                this.transform.position = pos;
            }
            else if (nextDirection == 1)
            {
                Vector2 pos = this.transform.position;
                this.transform.eulerAngles = new Vector3(0, 0, 180);
                pos.y = pos.y - 0.5f;
                this.transform.position = pos;
            }
            else if (nextDirection == 2)
            {
                Vector2 pos = this.transform.position;
                this.transform.eulerAngles = new Vector3(0, 0, 270);
                pos.x = pos.x + 0.5f;
                this.transform.position = pos;
            }
            else if (nextDirection == 3)
            {
                Vector2 pos = this.transform.position;
                this.transform.eulerAngles = new Vector3(0, 0, 90);
                pos.x = pos.x - 0.5f;
                this.transform.position = pos;
            }

            direction = nextDirection;
        }
	}


    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.tag == "Food")
        {
            score = score + 1;
            ate = true;
        }
        else
        {
            if (started == false)
            {
                Destroy(parent);
                net.AddFitness((score*1000));
                net.AddFitness(secondsLived);
                dead = true;
                Debug.Log("CRASHED");
                //Scene scene = SceneManager.GetActiveScene(); SceneManager.LoadScene(scene.name);
            }
        }
        
    }

}
