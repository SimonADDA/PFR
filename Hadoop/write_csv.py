 # Récupération des PDF
import arxiv
import csv

#You can choose here how many pdf you want. 
max_results=100

search = arxiv.Search(
  query = "Blockchain",
    max_results = max_results,
  sort_by = arxiv.SortCriterion.SubmittedDate
)

rows = [['ID', 'Title', 'Authors', 'Date'] ]
for result in search.results():
    rows.append(list([str(result.entry_id), str(result.title), str(result.authors), str(result.published)]))
    print([str(result.entry_id), str(result.title), str(result.authors), str(result.published)])

# print(rows)

with open('Hadoop/dataset.csv', 'w',newline ='') as f:
    write = csv.writer(f)
    write.writerows(rows)

   
      
    

