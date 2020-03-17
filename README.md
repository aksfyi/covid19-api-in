

## **Api-covid19-in**

A simple api to track covid19 cases in India

**Endpoints**

All requests must be made to the url :
[https://api-covid19-in.herokuapp.com/](http://api-covid19-in.herokuapp.com/)

**Total cases in India :**

    GET /getdata

**Output:**

       {
	      "deaths": "2", 
	      "infected": "99", 
	      "recovered": "13", 
	      "total_cases": "114"
       }

**Get cases by states**
   

    GET /getdata?state={state_name}

**Request:**

    /getdata?state=Jammu%20and%20Kashmir

    /getdata?state=Maharashtra

**Output:**

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
   
**To retrieve data of All states :**

    /getdata?state=all

**Get news :**

Returns first page ( nos : 12 ) of [India Today (covid19 news)](https://www.indiatoday.in/coronavirus-covid-19-outbreak)

    GET  /news
**Output:**

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

Api fetches covid19 cases from :
[https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_India](https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_India)
News from : 
[India Today (covid19 news)](https://www.indiatoday.in/coronavirus-covid-19-outbreak)


**Credits:**

 - [India Today (covid19 news)](https://www.indiatoday.in/coronavirus-covid-19-outbreak)
 - [Wikipedia](https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_India)
 - [Ministry of Health and Welfare , India](https://www.mohfw.gov.in/)
 - [Stackedit](https://stackedit.io/)

 **License :**

The data is available only for research and academic purposes. 


