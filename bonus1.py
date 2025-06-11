contents = ["All carrots are to be sliced longitudinally", "The carrots were reportedly sliced longitudinally", "All sliced carrots were sliced longitudinally"]
filenames = ['doc.txt','reports.txt','presentation.txt']


for contents,filenames in zip(contents,filenames):
    file = open(f"files/{filenames}",'w')
    file.write(contents)