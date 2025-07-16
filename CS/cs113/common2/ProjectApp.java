import java.util.Random;

public class ProjectApp{

public static void main(String[]args){
    Project template = new Project("Research Project:",10);
    System.out.println(template);
    Project project = new Project("Big Data",0);
    Random rand = new Random();
    int days = 0;
    while(project.getPages()<template.getPages()){
      int page = rand.nextInt(4);
      project.addPages(page);
      System.out.println("DAY:"+days+"Pages added"+page);
      days++;
       
    }
System.out.println(project);
System.out.println("Number of days to complete: " +days);










    
}












}