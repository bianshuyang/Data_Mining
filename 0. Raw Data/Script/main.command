#!/bin/bash

# Start and end page numbers
start_page=29187
end_page=29999

# Function to download a page
download_page() {
    page=$1
    wget "https://thegradcafe.com/survey/index.php?page=$page" -O "page_$page.html"
    sleep 1
}

export -f download_page

# Use parallel to download pages
seq $start_page $end_page | parallel -j 10 download_page
