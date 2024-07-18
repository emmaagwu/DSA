# Pascal Triangle Algorithm

- The solution would return a list of lists.
- Create an empty container where to store the list and return it when you finish.
- If `n` is not an integer or it is less than or equal to zero, return the empty container.
- Otherwise, fill the container with `[1]` which is the first row.
- Create a container for creating and adding new rows.
- The container must always begin with `[1]` and end with `[1]` when finished.
- To fill the container, move to the previous row and add the elements of that row in pairs to get the values in between the beginning and the end of the row.
- For example, to generate the third row from the second row `[1, 2, 1]`, add `1 + 2` to get `3`, and `2 + 1` to get `3`, resulting in `[1, 3, 3, 1]`.
- Continue this process until you have generated `n` rows.
- Return the container holding all the rows of Pascal's triangle.
