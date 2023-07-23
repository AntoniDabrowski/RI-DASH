# RI-DASH
RI-DASH is subset of our company page https://biomedical.dev6.rightinformation.com/. The purpose of this repository is to show the community that the top UI/UX standards can be achieved using DASH framework. We recommend checking out our portfolio tab to see the full demo.

## Local set-up
To ensure successful local run I recommend using docker. Run terminal in repository root. Next, use following commands to create a container.
```bash
docker-compose build
docker-compose up
```

Add your own ChatGPT API-KEY in .env file, in order to use the contextual chatbot.


## Structure
```bash
$ tree
.
│   # All the graphics, stylesheets and scripts used in the project
├── assets
│
│   # cache for chroma database - uesd in contextual chatbot
├── cache
│
│   # results of the genomic analysis - used for creating the plots
├── data
│
│   # chroma database - stores semantic embeddings of analysed publications chunks
├── database
│
│   # body of each displayed page
├── pages
│
│   # all the functionality and callbacks for pages
├── utils
│
│   # stores environmental variables
├── .env
│
│   # main file; run this to start the app
└── app.py
```