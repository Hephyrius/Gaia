using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Spawner : MonoBehaviour {

	// Use this for initialization
	void Start () {
        int positionX = (int)Random.Range(-14f, 14f);
        int positionY = (int)Random.Range(-14f, 14f);

        float posx = positionX * 0.5f;
        float posy = positionY * 0.5f;

        Vector2 position = new Vector2(posx, posy);
        this.transform.position = position;
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.tag == "Snake" || collision.gameObject.tag == "Body")
        {
            int positionX = (int)Random.Range(-14f, 14f);
            int positionY = (int)Random.Range(-14f, 14f);

            float posx = positionX * 0.5f;
            float posy = positionY * 0.5f;

            Vector2 position = new Vector2(posx, posy);
            this.transform.position = position;
        }
    }

    private void OnTriggerExit2D(Collider2D collision)
    {
        this.GetComponent<SpriteRenderer>().color = Color.white;
    }
}
