public class Project {

    private String title;
    private int pages;

    //constructor

    public Project(String title, int pages){
        this.title= title;
        this. pages=pages;

    }

    //setter for title
    public void setTitle(String title){
        this.title = title;
    }

    //getter pages

    public int getPages(){
        return pages;
    }

    //addpages Method

    public int addPages(int morePages){

        pages = pages + morePages;
        return morePages;
    }

    //toString
    public String toString(){
        return "Project: "+ title +   ", Number of pages: "  + pages;


    }


    //equals method
    public boolean equals(Project other){
        boolean title = this.title.equals(other.title);
        if(this.pages == other.getPages() && title){
            return true;
        }

        else{
            return false;
        }
    }



}


