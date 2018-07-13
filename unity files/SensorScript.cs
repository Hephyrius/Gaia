using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SensorScript : MonoBehaviour {

    public float distance;
    public int type;
    public GameObject endobj;

    // Max and min readings
    private const float MAX_DIST = 100000f;
    private const float MIN_DIST = 0.01f;


    [SerializeField]
    private LayerMask wallLayer;

    [SerializeField]
    private LayerMask bodyLayer;

    [SerializeField]
    private LayerMask foodLayer;


    public float distanceWall;
    public float distanceFood;
    public float distanceBody;

    // Unity method for updating the simulation
    void FixedUpdate()
    {
        //Calculate direction of sensor
        Vector2 direction = endobj.transform.position - this.transform.position;
        direction.Normalize();

        //Send raycast into direction of sensor
        RaycastHit2D wallhit = Physics2D.Raycast(this.transform.position, direction, MAX_DIST, wallLayer);

        //Check distance
        if (wallhit.collider == null)
        {
            distanceWall = MAX_DIST;
        }
        else
        {
            distanceWall = wallhit.distance;
        }

        //Send raycast into direction of sensor
        RaycastHit2D bodyhit = Physics2D.Raycast(this.transform.position, direction, MAX_DIST, bodyLayer);

        //Check distance
        if (bodyhit.collider == null)
        {
            distanceBody = MAX_DIST;
        }
        else
        {
            distanceBody = bodyhit.distance;
        }

        //Send raycast into direction of sensor
        RaycastHit2D foodhit = Physics2D.Raycast(this.transform.position, direction, MAX_DIST, foodLayer);

        //Check distance
        if (foodhit.collider == null)
        {
            distanceFood = MAX_DIST;
        }
        else
        {
            distanceFood = foodhit.distance;
        }

    }
}
