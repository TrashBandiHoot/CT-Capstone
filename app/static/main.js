var query = ''
var URL = ''
window.onload = function(){
document.getElementById('enter').onclick = function(){
    //get the info for the query out of the search bar and turn it
    //into the URL to feed to the AJAX call
    query = document.getElementById('searchbar').value
    document.getElementById('searchbar').value = ''
    URL = 'https://www.googleapis.com/books/v1/volumes?q='+query

    clearPrevious();
    $.ajax({
      url: URL.toString(),
      dataType: 'json',
      success: function(data){
      console.log(data);

        for(i=0; i<10; i++){

            var booki = 'book'+(i+1)

            //create rows
            //images row
            var imgRow = document.createElement('div')
            imgRow.className = "row imgRow"
            document.getElementById(booki).appendChild(imgRow)

            //title and price row
            var titlePriceRow = document.createElement('div')
            titlePriceRow.className = "row titlePriceRow"
                //title column
                var titleDiv = document.createElement('div')
                titleDiv.className = "col-md-8 title"
                titlePriceRow.appendChild(titleDiv)
                //price column
                var priceDiv = document.createElement('div')
                priceDiv.className = "col-md-2 col-md-offset-1 price"
                titlePriceRow.appendChild(priceDiv)

                document.getElementById(booki).appendChild(titlePriceRow)

            //author row
            var authorRow = document.createElement('div')
            authorRow.className = "row authorRow"
               //author column
                var authorDiv = document.createElement('div')
                authorDiv.className = "col-md-12 author"
                authorRow.appendChild(authorDiv)

                document.getElementById(booki).appendChild(authorRow)

            //description row
            var descriptionRow = document.createElement('div')
            descriptionRow.className = "row descriptionRow"
               //description column
                var descriptionDiv = document.createElement('div')
                descriptionDiv.className = "col-md-12 description"
                descriptionRow.appendChild(descriptionDiv)

                document.getElementById(booki).appendChild(descriptionRow)

            //populate the rows with the data
            //image data
            var img = document.createElement('img')
            img.src = data.items[i].volumeInfo.imageLinks.smallThumbnail
            document.getElementsByClassName('imgRow')[i].appendChild(img)

            //title data
            var title = document.createElement('h1')
            title.innerHTML =  data.items[i].volumeInfo.title
            document.getElementsByClassName('title')[i].appendChild(title)

            //price data
            var price = document.createElement('h1')
            if(data.items[i].saleInfo.listPrice!=undefined){
                price.innerHTML = '$' + data.items[i].saleInfo.listPrice.amount
            }else{
                price.innerHTML = "N/A"
            }
            document.getElementsByClassName('price')[i].appendChild(price)

            //author data
            var author = document.createElement('p')
            author.innerHTML = 'By: ' +  data.items[i].volumeInfo.authors[0]
            document.getElementsByClassName('author')[i].appendChild(author)

            //description data
            var description = document.createElement('p')
            description.innerHTML =  data.items[i].volumeInfo.description
            document.getElementsByClassName('description')[i].appendChild(description)

        }//end for loop
      }//end ajax success function
    })//end ajax call
}//end click function

function clearPrevious(){
    for(i=0; i<10; i++){
        var booki = 'book'+(i+1)
        
        //delete rows
        //images row
        removeElementsByClass('imgRow')

        //title and price row
        removeElementsByClass('titlePriceRow')   

        //author row
        removeElementsByClass('authorRow')   

        //description row
        removeElementsByClass('descriptionRow')
  
    }//end for loop
}//end clearPrevious function

function removeElementsByClass(className){
    var elements = document.getElementsByClassName(className);
    for(j=0; j<elements.length; j++){
        elements[0].parentNode.removeChild(elements[0]);
    }
}};