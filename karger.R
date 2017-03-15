setwd('...')

processFile <- function(filepath) {
  # Read input file and output a list of vectors containing vertices and edges (called adjacency list)
  # The first element of a vector represents a vertex (or node)
  # The remaining elements of the vector represents all vertices that the first element is adjacent to
  # Undirected pairs of vertices are called unordered edges
  # Each of the remaining elments shares an unordered edge with the first element
  con = file(filepath, "r")
  lst <- list()
  lines <- readLines(con, n = -1)
  j <- 1
  for (i in 1:length(lines)) {
    if (lines[i] != "") {
      line <- as.numeric(read.table(text = lines[i], sep = ""))
      lst[[j]] <- line[!is.na(line)]
      j <- j + 1
    }
  }
  close(con)
  return (lst)
}

sample2 <- function(x) {
  # When the function sample(x, 1) is used on a single number x, 
  # it will return a random number in 1:x
  # This function prevents that and output x
  if (length(x) <= 1) {
    return(x)
  } else {
    return(sample(x,1))
  }
}

karger <- function(dat, num_sim) {
  # This function uses Karger's random contraction to find the minimun number of edges that
  # cross a cut through the graph (minimun cut)
  # Arguments:
  #    dat: the ajacency list
  #    num_sim: the number of simulations
  count <- 10000
  
  for (s in 1:num_sim) {
    adjacency_list <- dat
    
    # Randomly contracting the adjacency list till the size of the list becomes 2
    while (length(adjacency_list) > 2) {
      # Construct a list of remaining vertices after each contraction
      vertex <- numeric()
      for (i in 1:length(adjacency_list)) {
        vertex[i] <- adjacency_list[[i]][1]
      }
      
      # Randomly select the first vertex
      v1 <- sample2(vertex)
      v1.location <- which(vertex == v1)
      
      # Randomly select the second vertex
      v2 <- sample2(adjacency_list[[v1.location]][-1])
      v2.location <- which(vertex == v2)
      
      ## Merge the second vertex with the first vertex: 
      
      # Step 1: Copy the edges of the second vertex to the first vertex
      adjacency_list[[v1.location]] <- c(adjacency_list[[v1.location]], 
                                         adjacency_list[[v2.location]][-1])
      
      # Step 2: Replace the second vertex with the first vertex in all other vertices' edges
      for (i in which(vertex %in% adjacency_list[[v2.location]][-1])) {
        adjacency_list[[i]][-1][adjacency_list[[i]][-1]%in%v2] <- v1
      }
      
      # Step 3: Remove redundant internal edges in the first vertex
      adjacency_list[[v1.location]] <- c(v1, adjacency_list[[v1.location]][-1][!adjacency_list[[v1.location]][-1]%in%v1])
      
      # Step 4: Delete the second vertex. Merge is completed
      adjacency_list[v2.location] <- NULL
    }
    
    # Select the minimum number of edges
    min_cut <- length(adjacency_list[[1]]) - 1
    if (min_cut < count) {
      count <- min_cut
    }
  }
  return(count)
}

# Example
dat <- processFile('kargerMinCut.txt')
karger(dat, 400)
# The minimum cut of this example is 17
