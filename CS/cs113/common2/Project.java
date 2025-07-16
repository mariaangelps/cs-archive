public class Project{
    private String title;
    private int pages;
public Project(String newTitle, int newPages){

    title=newTitle;
    pages=newPages;
}

public int getPages(){
    return pages;
}
public void setTitle(String newTitle){
    title = newTitle;

}
public void addPages(int addition){
    pages+=addition;
}

public String toString(){
    return "Project Title:" + title + "Number of Pages: " + pages;
}


public boolean equals(Project other){
    return (pages == other.pages&&title.equals(other.title));
   

}


}















    
