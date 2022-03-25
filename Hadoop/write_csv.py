 # Récupération des PDF
import arxiv
import csv

#You can choose here how many pdf you want. 
max_results=500

search = arxiv.Search(
  query = "AI",
    max_results = max_results,
  sort_by = arxiv.SortCriterion.SubmittedDate
)

rows = [['ID', 'Title', 'Authors', 'Date','Categorie'] ]
for result in search.results():
    rows.append(list([str(result.entry_id), str(result.title),str(result.categories), str(result.authors), str(result.published)]))

with open('Hadoop/dataset.csv', 'w',newline ='') as f:
    write = csv.writer(f)
    write.writerows(rows)

   
      
    

