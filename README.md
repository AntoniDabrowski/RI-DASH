# RI-DASH
RI-DASH is a subset of our [company page](https://biomedical.dev6.rightinformation.com/). The purpose of this repository is to show the community that the **top UI/UX** standards can be achieved using the **DASH** framework. We recommend checking out our portfolio tab to see the full demo[<sup>\[1\]</sup>](https://biomedical.dev6.rightinformation.com/genomic-analysis)[<sup>\[2\]</sup>](https://biomedical.dev6.rightinformation.com/lipidomic-analysis).

## Highlights
<div style="display: grid">
    <div style="display: grid; width: 650px; margin-left: auto; margin-right: auto">
        <img src="https://live.staticflickr.com/65535/53065642139_efa415c4b5_c.jpg">
        Figure 1: Analysis of the most discriminating genes for thyroid and kidney cancer.
    </div>
    <div style="display: grid; width: 650px; margin-left: auto; margin-right: auto; padding-top: 50px">
        <img src="https://live.staticflickr.com/65535/53065475846_636596ae50_h.jpg">
        Figure 2: Visualization of automatic information retrieval. Expression of crucial insights from the data.
    </div>
    <div style="display: grid; width: 650px; margin-left: auto; margin-right: auto; padding-top: 50px"> 
        <img src="https://live.staticflickr.com/65535/53065855240_ebc2acf556_h.jpg">
        Figure 3: Contextual chatbot. The user can ask questions about the relevant publication and the chatbot will answer them.
    </div>
</div>

## Local set-up
To ensure a successful local run I recommend using docker. Run the terminal in the repository root. Next, use the following commands to create a container.
```bash
docker-compose build
docker-compose up
```

Add your own [OpenAI API-KEY](https://openai.com/blog/openai-api) in .env file, in order to use the contextual chatbot.


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