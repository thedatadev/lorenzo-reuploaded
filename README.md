# Lorenzo (re-uploaded)

https://user-images.githubusercontent.com/48514825/130351300-fbe5143e-6c99-4666-9e95-86320230df72.mp4


## NOTE:
This is a re-upload of a university project without API secrets/keys and other sensitive information. My role in this project was to write the entire client as well as the majority of the API server. The project started on 02/08/18 and ended on 21/10/18. A complete log of all the work I had done on this project can be found in the work-log.txt file.

## Problem
Traditional search forms vary from webpage to webpage and come in different structures. What if we could standardize the way search forms are implemented to make them webpage-agnostic whilst improving user experience?

## Implementation
Current state-of-the-art natural language processing algorithms are able to pick up entities within text. This can be used to automatically pick out search parameters within free-form text queries.

## Technology
	- Vue/Vuex
	- Python, Flask
	- PostgreSQL, RDS
	- Google Dialogflow

## Challenges
	- Creating an intuitive chatbot interface
	- Figuring out an appropriate layout for desktop devices for an app that was designed with mobile/tablet in mind (eventually gave up due to time constraints and stuck with a mobile-only design)
	- Balancing the trade-off with complexity of search queries, which can often take along time, with the fluidity of a conversation which needs to be as responsive as possible

## Further work
    - Figuring out a desktop design
