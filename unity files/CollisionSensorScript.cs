using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CollisionSensorScript : MonoBehaviour {


    public bool triggered;
    float trigTimer = 0;
    public float distanceWall;
    public float distanceFood;
    public float distanceBody;

    GameObject wall;
    GameObject food;
    GameObject body;

    bool wallDetected;
    bool foodDetected;
    bool bodyDetected;

    private void Update()
    {
        if(wallDetected == true)
        {
            distanceWall = Vector2.Distance(this.transform.position, wall.transform.position);
        }
        else
        {
            distanceWall = -1;
        }

        if (foodDetected == true)
        {
            distanceFood = Vector2.Distance(this.transform.position, food.transform.position);
        }
        else
        {
            distanceFood = -1;
        }

        if (bodyDetected == true)
        {
            distanceBody = Vector2.Distance(this.transform.position, body.transform.position);
        }
        else
        {
            distanceBody = -1;
        }
    }



    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.tag == "Border")
        {
            wall = collision.gameObject;
            wallDetected = true;
        }
        else if (collision.gameObject.tag == "Body")
        {
            body = collision.gameObject;
            bodyDetected = true;

        }
        else if (collision.gameObject.tag == "Food")
        {
            food = collision.gameObject;
            foodDetected = true;

        }
    }

    private void OnTriggerExit2D(Collider2D collision)
    {
        if (collision.gameObject.tag == "Border")
        {
            wall = new GameObject();
            wallDetected = false;
        }
        else if (collision.gameObject.tag == "Body")
        {
            body = new GameObject();
            bodyDetected = false;

        }
        else if (collision.gameObject.tag == "Food")
        {
            food = new GameObject();
            foodDetected = false;

        }
    }
}
