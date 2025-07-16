import java.util.Random;

public class ProjectApp{

    public static void main(String [] args) {
        Project template = new Project("Research Project",10);
        System.out.println(template.toString());
        Project project = new Project("Big Data",0);
        Random rand = new Random();

        int days =0;
        for(int d= 1; d<=7 ; d++){
            int p = rand.nextInt(4);
            project.addPages(p);
            days++;
            System.out.println("Day 1: " + "Pages added: " + p);

        }

        System.out.println(project.toString());
        System.out.println("Number of Days to complete: " + days);

    }


}



