from flask import Flask,request
from pprint import pprint
from main import generate_uber_deeplink
#from coordinates import get_coordinates
from placetocord import placetocoord
#from latitude_converter import get_coordinates

app=Flask(__name__)

@app.route('/taxi_search',methods=['POST'])
def taxi_details():
    data=request.get_json(force=True)      
    pprint(data)
    sessioninfo=data['sessionInfo']
    parameters=sessioninfo['parameters']
    dropoff_nickname=parameters['destination-place']["original"]
    #dropoff_lat,dropoff_lng=placetocoord(dropoff_nickname)
    pickup_lat = parameters['latitude']
    pickup_lng = parameters['longitude']
    result=placetocoord(dropoff_nickname,pickup_lat,pickup_lng)
    dropoff_lat=result["lat"]
    dropoff_lng=result["lng"]

    client_id = "ozYFgFCbquB7cYJF9rW_3_0e5vhxcHmi"
   
    pickup_nickname = parameters['location']
    #dropoff_lat = 28.5535
    #dropoff_lng = 77.2588
    #dropoff_nickname = "lotus temple"

    result=generate_uber_deeplink(client_id,pickup_lat,pickup_lng,pickup_nickname,dropoff_lat,dropoff_lng,dropoff_nickname)
#[Know more about the event]({i['event_link']})
    response={
          "fulfillmentResponse": {
                                  "messages": [
                                      {
                                        "responseType": "RESPONSE_TYPE_UNSPECIFIED",
                                        "channel": "",

                                        #Union field message can be only one of the following:
                                        "payload": {
                          "botcopy": [
            {
            "card": {
                "action": {
                "buttons": [
                    {
                    "action": {
                        "link": {
                        "target": "_blank",
                        "url": f"{result}"
                        }
                    },
                    "title": "Check taxi fares"
                    },
                    {
                    "action": {
                        "message": {
                        "command": "Pricing",
                        "type": "training"
                        }
                    },
                    "title": ""
                    }
                ]
                },
                "body": "",
                "image": {
                "alt": "Image of a cat",
                "url": "https://images.pexels.com/photos/462867/pexels-photo-462867.jpeg?cs=srgb&dl=pexels-kai-pilger-462867.jpg&fm=jpg"
                },
                "subtitle": f"From {pickup_nickname}\n{'⇅'} \n To {dropoff_nickname}",
                "title": ""
            }
            }
        ]
        }
                            }

                                  ]

                        }
                    
                }
            
    return response


    #return response

'''{
  "botcopy": [
    {
      "card": {
        "action": {
          "buttons": [
            {
              "action": {
                "link": {
                  "target": "_blank",
                  "url": "https://botcopy.com"
                }
              },
              "title": "Linkout Button"
            },
            {
              "action": {
                "message": {
                  "command": "Pricing",
                  "type": "training"
                }
              },
              "title": "Message Button"
            }
          ]
        },
        "body": "Card body",
        "image": {
          "alt": "Image of a cat",
          "url": "https://homepages.cae.wisc.edu/~ece533/images/cat.png"
        },
        "subtitle": "Card subtitle",
        "title": "Card title"
      }
    }
  ]
}
'''


#deeplink = generate_uber_deeplink(client_id, pickup_lat, pickup_lng, pickup_nickname, dropoff_lat, dropoff_lng, dropoff_nickname)


if __name__=='__main__':
    app.run(debug=True,port=9900)







