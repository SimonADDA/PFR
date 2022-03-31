 # Récupération des PDF
import arxiv
import csv

max_results=500

search = arxiv.Search(
  query = "AI",
    max_results = max_results,
  sort_by = arxiv.SortCriterion.SubmittedDate
)

rows = [['ID', 'Title', 'Authors', 'Date','Year','Categorie'] ]
for result in search.results():
    rows.append(list([str(result.entry_id), str(result.title), str(result.authors), str(result.published),str(result.categories)]))

with open('Hadoop/dataset.csv', 'w',newline ='') as f:
    write = csv.writer(f)
    write.writerows(rows)

   
      
    

