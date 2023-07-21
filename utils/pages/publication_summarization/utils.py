import pandas as pd

table_df_path = './data/publication_summarization/table_content_short.pickle'

table_df = pd.read_pickle(table_df_path)
table_data = [{"type": "Genes", "Thyroid_Carcinoma": table_df.loc["Thyroid_Carcinoma"]["Genes"],
               "ccRCC": table_df.loc["ccRCC"]["Genes"]},
              {"type": "Proteins", "Thyroid_Carcinoma": table_df.loc["Thyroid_Carcinoma"]["Proteins"],
               "ccRCC": table_df.loc["ccRCC"]["Proteins"]},
              {"type": "Lipids/fats", "Thyroid_Carcinoma": table_df.loc["Thyroid_Carcinoma"]["Lipids/fats"],
               "ccRCC": table_df.loc["ccRCC"]["Lipids/fats"]},
              {"type": "Metabolites", "Thyroid_Carcinoma": table_df.loc["Thyroid_Carcinoma"]["Metabolites"],
               "ccRCC": table_df.loc["ccRCC"]["Metabolites"]}]
table_columns = [{"name": "", "id": "type"}, {"name": "Thyroid Carcinoma", "id": "Thyroid_Carcinoma"},
                 {"name": "ccRCC", "id": "ccRCC"}]

table_description = \
    """The table below shows key insights on a given topic based on analysis of over 10k publications collected from 
    online repository OpenAlex. The analysis was performed by our specialized information retrieval system.
    It ranked the most important elements for a given topic and provided the most relevant publications.
    Then, the system created semantic embeddings of paragraphs and used them to answer question about the relation
    between two topics. The table below shows the most important elements for two types of cancer."""