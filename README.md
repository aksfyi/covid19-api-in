## PLEASE CHECK UPDATED DOCS HERE :http://api-covid19-in.herokuapp.com/





## **Api-covid19-in**

A simple api to track covid19 cases in India. Updated every 30 mins.

**Endpoints**

All requests must be made to the url :
[https://api-covid19-in.herokuapp.com/](http://api-covid19-in.herokuapp.com/)

**Total cases in India :**

[/getdata](https://api-covid19-in.herokuapp.com/getdata)

    GET /getdata

**Response (JSON):**

      {
      "results": [
        {
          "active": "391", 
          "deaths": "7", 
          "migrated": "1", 
          "recoveries": "23", 
          "total": "415"
        }
      ]
    }

 - Recoveries  - cured / discharged
 - Active cases = total - ( recoveries + migrated)
 - Data from - [https://www.mohfw.gov.in/](https://www.mohfw.gov.in/)

**Get cases by states**

   [/getdata?state=Maharashtra](https://api-covid19-in.herokuapp.com/getdata?state=Maharashtra)

    GET /getdata?state={state_name}

**Request:**

    GET /getdata?state=Jammu%20and%20Kashmir

    GET /getdata?state=Maharashtra

**Response (JSON):**

    {
      "results": [
        {
          "active": "3", 
          "deaths": "0", 
          "recoveries": "0", 
          "state": "Jammu and Kashmir", 
          "total": "3"
        }
      ]
    }

 - Data from : [Wikipedia](https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_India)

   
**To retrieve data of All states :**
  [/getdata?state=all](https://api-covid19-in.herokuapp.com/getdata?state=all)

   

     GET /getdata?state=all

**Sorting results of all states**

      /getdata?state=all&sortkey={key}_{order}


**Order :**

  - Default order : Alphabetic 
 - asc - Sorts items in ascending order
 - des - Sorts items in descending order

**Example**
  [/getdata?state=all&sortkey=active_des](https://api-covid19-in.herokuapp.com/getdata?state=all&sortkey=active_des)


**Get daily data :**
	

[/dailydata](https://api-covid19-in.herokuapp.com/dailydata)

    GET  /dailydata?len={default value = 20}
   
   **Response (JSON):**
   

    GET /dailydata?pretty=1&len=2
    
    
    {
      "results": [
        {
          "cases": [
            {
              "new": "50", 
              "total": "223"
            }
          ], 
          "date": "2020-03-20", 
          "deaths": [
            {
              "new": "0", 
              "total": "4"
            }
          ]
        }, 
        {
          "cases": [
            {
              "new": "60", 
              "total": "283"
            }
          ], 
          "date": "2020-03-21", 
          "deaths": [
            {
              "new": "0", 
              "total": "4"
            }
          ]
        }
      ]
    }

 - Data from : [Wikipedia](https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_India)


**Get news :**

Returns first page ( nos : 12 ) of [India Today (covid19 news)](https://www.indiatoday.in/coronavirus-covid-19-outbreak)


[/news](https://api-covid19-in.herokuapp.com/news)
 

       GET  /news

**Response (JSON):**

    {
      "results": [
        {
          "image":  ... , 
          "news_link":  ..., 
          "snippet":  ... , 
          "title": ...
        }
        ]
    }

**Pretty print:**

    /getdata?state=all&pretty=1
    /news?pretty=1

**Errors:**

    {
      "error": <error related info>
    }

**Data Source**

 - Api fetches covid19 cases from : [Wikipedia - 2020
   covid19-India](https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_India)
 - News from :  [India Today (covid19
   news)](https://www.indiatoday.in/coronavirus-covid-19-outbreak)

**Credits:**

 - [India Today (covid19 news)](https://www.indiatoday.in/coronavirus-covid-19-outbreak)
 - [Wikipedia](https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_India)
 - [Ministry of Health and Welfare , India](https://www.mohfw.gov.in/)
 - [Stackedit](https://stackedit.io/)

**Projects developed using this api**

 -  https://in-covid19.netlify.app

 **License :**

The data is available only for research and academic purposes. 


