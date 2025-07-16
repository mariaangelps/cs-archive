public abstract class Shape {
    protected String shapeName;
    public Shape (String shapeName){
        this.shapeName = shapeName;
    }
    public abstract double area(); //---> abstract method, no body
    public String toString (){
        return shapeName;
    }

}
