# Pagination Project

## Overview

This project focuses on implementing pagination techniques for a dataset of popular baby names. The project includes tasks to create simple pagination, hypermedia pagination, and deletion-resilient pagination.

## Learning Objectives

By the end of this project, you should be able to:
- Paginate a dataset with simple page and page_size parameters.
- Paginate a dataset with hypermedia metadata.
- Paginate in a deletion-resilient manner.

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Code should use the `pycodestyle` style (version 2.5.*).
- The length of files will be tested using `wc`.
- All modules should have documentation.
- All functions should have documentation.
- All functions and coroutines must be type-annotated.

## Setup

Download the dataset file `Popular_Baby_Names.csv` and place it in the project directory.

## Tasks

### Task 0: Simple Helper Function

Write a function named `index_range` that takes two integer arguments `page` and `page_size`.

- The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.
- Page numbers are 1-indexed, i.e., the first page is page 1.

**File:** `0-simple_helper_function.py`

![Simple Helper Function](https://via.placeholder.com/600x400?text=Simple+Helper+Function+GIF)

### Task 1: Simple Pagination

Copy `index_range` from the previous task and implement a `Server` class with a method `get_page`.

- The `get_page` method takes two integer arguments `page` with default value 1 and `page_size` with default value 10.
- Use `assert` to verify that both arguments are integers greater than 0.
- Use `index_range` to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset.
- If the input arguments are out of range for the dataset, an empty list should be returned.

**File:** `1-simple_pagination.py`

![Simple Pagination](https://via.placeholder.com/600x400?text=Simple+Pagination+GIF)

### Task 2: Hypermedia Pagination

Replicate code from the previous task and implement a `get_hyper` method.

- The `get_hyper` method takes the same arguments (and defaults) as `get_page` and returns a dictionary containing the following key-value pairs:
  - `page_size`: the length of the returned dataset page.
  - `page`: the current page number.
  - `data`: the dataset page (equivalent to return from the previous task).
  - `next_page`: number of the next page, `None` if no next page.
  - `prev_page`: number of the previous page, `None` if no previous page.
  - `total_pages`: the total number of pages in the dataset as an integer.
- Reuse `get_page` in your implementation.

**File:** `2-hypermedia_pagination.py`

![Hypermedia Pagination](https://via.placeholder.com/600x400?text=Hypermedia+Pagination+GIF)

### Task 3: Deletion-Resilient Hypermedia Pagination

Implement a `get_hyper_index` method with two integer arguments: `index` with a `None` default value and `page_size` with default value of 10.

- The method should return a dictionary with the following key-value pairs:
  - `index`: the current start index of the return page.
  - `next_index`: the next index to query with.
  - `page_size`: the current page size.
  - `data`: the actual page of the dataset.
- Use `assert` to verify that `index` is in a valid range.
- Ensure that if rows are removed from the dataset, the user does not miss items when changing pages.

**File:** `3-hypermedia_del_pagination.py`

![Deletion-Resilient Pagination](https://via.placeholder.com/600x400?text=Deletion-Resilient+Pagination+GIF)

## Usage

To run the scripts, use the following commands:

```sh
python3 0-main.py
python3 1-main.py
python3 2-main.py
python3 3-main.py
