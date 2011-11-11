library(plyr)
library(lda)
productive <- read.csv("cool_objects.csv", header=F)
colnames(productive) <- c("Person", "Thing", "Description", "URL")

productive_doclines <- ddply(.data=productive, c("Person"), 
                             summarise, 
                             things = paste(Thing, collapse=";")
                             #doclines = paste(Object, collapse=";")
                             )

lexical_doclines <- lexicalize(doclines=productive_doclines$things, sep=";")

lda_result <- lda.collapsed.gibbs.sampler(documents=lexical_doclines$documents,
                                          vocab=lexical_doclines$vocab,
                                          K=5, 
                                          alpha=0.1,
                                          eta=0.1,
                                          num.iterations= 100)
top.topic.words(lda_result$topics, num.words=5)