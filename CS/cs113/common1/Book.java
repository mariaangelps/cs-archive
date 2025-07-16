
//Homework #3
// Hola maria again desde el terminal
// Hola mari
//hola juan desde visual
//Maria Angel Palacios Sarmiento-3158891

package common1;

public class Book{

   //encapsulamiento
   private String title; //instance data del titulo
   private int pages; //instance data sobre las paginas
   
   //default constructor and initialize the data.
   public Book(){ 
      title= "Java Programming";
      pages= 200;
     }
 
   //getter method for each instance data     
   public String getBookTitle(){ //gets Book name
      return title;
     }
   
   public int getPageNumber(){ //gets pages number
      return pages;
   }
   
   //setter method for each instance
   public void setBookTitle(String newTitle){ //allows to modify the title
      title=newTitle;
      }
      
   public void setPageNumber(int newPages){//allows to modify the pages 
      pages=newPages;
      
      }
    
    //toString method--> it will only return a string
   public String toString(){
       return "The book's title is: " + title + "and the number of pages is: " +pages;
   
   
   }
   
   
 
}

