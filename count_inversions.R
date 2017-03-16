setwd('...')

sort_and_count <- function(a) {
  # Compute the number of inversions in the file given, where the ith row of the file indicates the ith entry of an array
  # and return the sorted array
  # Use divide and conquer algorithm
  n <- length(a)
  if (n == 1) {
    # Base case
    return (list(count = 0, a_sorted = a))
  } else {
    nby2 <- ceiling(n/2)
    x <- sort_and_count(a[1:nby2])
    y <- sort_and_count(a[(nby2+1):n])
    z <- merge_and_count_split_inv(x$a_sorted, y$a_sorted)
    count <- x$count + y$count + z$count
    a_sorted <- z$a_sorted
    return (list(count = count, a_sorted = a_sorted))
  }
}

merge_and_count_split_inv <- function(x,y) {
  # x and y are two sorted arrays
  # Count the number of occasions where elements in y are smaller than elements in x
  # Merge x and y into one sorted array
  n_x <- length(x)
  n_y <- length(y)
  n <- n_x + n_y
  d <- matrix(0, nrow = n, ncol = 1)
  i <- 1
  j <- 1
  count <- 0
  for (k in (1:n)) {
    if (j > n_y) { # End case
      d[k] <- x[i]
      i <- i+1
    } else if (i > n_x) { # End case
      d[k] <- y[j]
      j <- j+1
    } else {
      if (x[i] < y[j]) {
        d[k] <- x[i]
        i <- i+1
      } else if (y[j] < x[i]) {
        d[k] <- y[j]
        j <- j+1
        # If the jth element of y is smaller than the ith element of x,
        # it is smaller than all elements of x after the ith element
        count <- count + n_x - i + 1
      }
    }
  }
  return (list(count = count, a_sorted = d))
}

# Example
d <- as.matrix(read.table("IntegerArray.txt", sep = "", colClasses = c("numeric")))
sort_and_count(d)
