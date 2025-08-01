

# **Rediscovering Kanji**  

### **Objective / Goal**  
Make **kanji memorization easier** by discovering hidden patterns in radicals and clustering them meaningfully using **machine learning & deep learning**.  

### **Why This Matters?**  
1. **Current kanji learning is inefficient:**   
   - Rote memorization (writing & recalling) is time-consuming.  
   - Some kanji have logical visual structures, but most require brute-force learning.  

2. **Potential of Machine Learning in Kanji Learning:**  
   - Discover **hidden radical patterns** that are not explicitly taught.  
   - Identify **semantic relationships** between radicals and kanji.  
   - Create an **interactive kanji map** based on similarity to make learning intuitive.  

------
### Abstract

When it comes to learning Japanese, one of the biggest problem for any learner is Kanji. Specially for foreign students, unlike katakana and hiragana, students have a hard time learning, due to the complexity of Kanji, as it does not a logical pattern for learning, and heavily relies on writing practice, and rote memorization. This traditional apporach is time consuming and requires patiences, which makes many learners give up in the early stages of learning. To tackle this problem, we will explore what machine learning can do.

While some Kanji has logical structure made up of radicals, easy to understand, because of pictographical elements in it. But this is not true for all kanji. While some Kanji can be understood intuitively, while others becomes hard to remember when the Kanji has abstract meaning, because we are unable to form a clear mental image for these types of Kanji.

This research will explore with the applicaiton of machine learning and deep learning can be applied to uncover hidden patterns that may exist within Kanji, focusing on radical level Kanji and semantic relationships. The study aims to build a intuitive categorization system, we will cluster the kanji based on visual and meaning similarities. The ultimate goal is to make learning of Kanji easy with the application machine learning.

# Setting up and running docker

### BUILDING IMAGE
```
docker build -t rediscovering_k .
```


### RUNNING IMAGE
```
docker run -it -p 8888:8888 \
  -v $(pwd)/notebooks:/app/notebooks \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/models:/app/models \
  rediscovering_k
```

### START CONTAINER
```
jupyter lab --ip=0.0.0.0 --allow-root --no-browser --NotebookApp.token='9090'
```

### OPEN NOTEBOOK
[http://localhost:8888/lab](url:http://localhost:8888/lab)

