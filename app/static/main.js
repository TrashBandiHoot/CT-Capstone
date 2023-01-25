var query = ''
var URL = ''
window.onload = function(){
document.getElementById('enter').onclick = function(){
    // Get the info for the query out of the search bar and turn it into the URL to feed to the AJAX call

    query = document.getElementById('searchbar').value
    document.getElementById('searchbar').value = ''
    URL = 'https://www.googleapis.com/books/v1/volumes?q='+query

    // Must clear previous search results or there will be duplicates of every element when the books are loaded to the page
    clearPrevious();
    $.ajax({
      url: URL.toString(),
      dataType: 'json',
      success: function(data){
      console.log(data);

        for(i=0; i<10; i++){

            var booki = 'book'+(i+1)
            var itemi = 'item'+(i+1)

            // Create rows
            // Images row
            var imgRow = document.createElement('div')
            imgRow.className = "row imgRow"
            document.getElementById(booki).appendChild(imgRow)






            // Title and price row
            var titlePriceRow = document.createElement('div')
            titlePriceRow.className = "row titlePriceRow"
                // Title column
                var titleDiv = document.createElement('div')
                titleDiv.className = "col-md-6 title"
                titlePriceRow.appendChild(titleDiv)
                // Price column
                var priceDiv = document.createElement('div')
                priceDiv.className = "col-md-2 price"
                titlePriceRow.appendChild(priceDiv)

                document.getElementById(booki).appendChild(titlePriceRow)

            // Author row
            var authorRow = document.createElement('div')
            authorRow.className = "row authorRow"
               // Author column
                var authorDiv = document.createElement('div')
                authorDiv.className = "col-md-12 author"
                authorRow.appendChild(authorDiv)



                // Book column
                var add_book = document.createElement('form') // is a node
                add_book.className = "add_book"
                book_id = data.items[i].id
                add_book.action = 'https://coding-temple-capstone.herokuapp.com/api/addbook/' + book_id
                add_book.method = 'POST'
                document.getElementById(booki).appendChild(add_book)

                document.getElementById(booki).appendChild(authorRow)


                
            // Description row
            var descriptionRow = document.createElement('div')
            descriptionRow.className = "row descriptionRow"
               // Description column
                var descriptionDiv = document.createElement('div')
                descriptionDiv.className = "col-md-12 description"
                descriptionRow.appendChild(descriptionDiv)

                document.getElementById(booki).appendChild(descriptionRow)

            // Populate the rows with the data
            // Image data
            var img = document.createElement('img')
            img.src = data.items[i].volumeInfo.imageLinks.smallThumbnail
            document.getElementsByClassName('imgRow')[i].appendChild(img)



            // Book data
            var book_button = document.createElement('button')
            book_button.setAttribute('type', 'submit')
            book_button.setAttribute('value', data.items[i].id)
            book_button.innerHTML = 'Add Book'
            document.getElementsByClassName('add_book')[i].appendChild(book_button)



            // Title data
            var title = document.createElement('h1')
            title.innerHTML =  data.items[i].volumeInfo.title
            document.getElementsByClassName('title')[i].appendChild(title)

            // Price data
            var price = document.createElement('h1')
            if(data.items[i].saleInfo.listPrice!=undefined){
                price.innerHTML = '$' + data.items[i].saleInfo.listPrice.amount
            }else{
                price.innerHTML = "N/A"
            }
            document.getElementsByClassName('price')[i].appendChild(price)

            // Author data
            var author = document.createElement('p')
            author.innerHTML = 'By: ' +  data.items[i].volumeInfo.authors[0]
            document.getElementsByClassName('author')[i].appendChild(author)

            // Description data
            var description = document.createElement('p')
            description.innerHTML =  data.items[i].volumeInfo.description
            document.getElementsByClassName('description')[i].appendChild(description)

        }// End for loop
      }// End ajax success function
    })// End ajax call
}// End click function

function clearPrevious(){
    for(i=0; i<10; i++){
        var booki = 'book'+(i+1)
        
        // Delete rows
        // Images row
        removeElementsByClass('imgRow')

        // Title and price row
        removeElementsByClass('titlePriceRow')   

        // Author row
        removeElementsByClass('authorRow')   

        // Description row
        removeElementsByClass('descriptionRow')

        // Add book button
        removeElementsByClass('add_book')

  
    }// End for loop
}// End clearPrevious function

function removeElementsByClass(className){
    var elements = document.getElementsByClassName(className);
    for(j=0; j<elements.length; j++){
        elements[0].parentNode.removeChild(elements[0]);
    }
}};


