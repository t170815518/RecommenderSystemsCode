# RecommenderSystemsCode
Python Implementation of Recommender Systems Handbook by Francesco Ricci and Lior Rokach
## Chapter 2.3 Neighborhood-based Recoomendation 
### Items' similarity 
Pearson's correlation:

<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;PC(x,y)=\frac{\sum_{u\in&space;U_{xy}}(r_{ux}-\bar&space;r_x)(r_{uy}-\bar&space;r_y)&space;}{\sqrt{\sum_{u\in&space;U_{xy}}(r_{ux}-\bar&space;r_x)^2&space;\sum_{u\in&space;U_{xy}}(r_{uy}-\bar&space;r_y)^2}}" title="PC(x,y)=\frac{\sum_{u\in U_{xy}}(r_{ux}-\bar r_x)(r_{uy}-\bar r_y) }{\sqrt{\sum_{u\in U_{xy}}(r_{ux}-\bar r_x)^2 \sum_{u\in U_{xy}}(r_{uy}-\bar r_y)^2}}">

To improve: 
1. Similarity based on items' genres? 
1. cold-start problem 
