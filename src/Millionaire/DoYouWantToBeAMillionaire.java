package Millionaire;
import java.awt.Color;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
import java.io.*;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;

public class DoYouWantToBeAMillionaire {
    
    public static int questionNumber = 1;
    public static boolean lifeline1Used = false;
    public static boolean lifeline2Used = false;
    public static int question = 0;
    public static boolean timerActive;
    public static int timerSum = 0;
    public static ArrayList<ArrayList<String>> questionsMain = new ArrayList<ArrayList<String>>();
    
    public static int getQuestion (){
        return question;
    }
       
    public static boolean getlifeline1Used(){
        return lifeline1Used;
    }
    
    public static void setlifeline1Used(){
        lifeline1Used = true;
    }
    
    public static boolean getlifeline2Used(){
        return lifeline2Used;
    }
    
    public static void setlifeline2Used(){
        lifeline2Used = true;
    }
    
    public static int getQuestionNumber(){
        return questionNumber;
    }
    
    public static void setQuestionNumber(){
        questionNumber += 1;
    }
    
    public static void test(){
        QuestionScreen.btnDHighlight = 2;
    }
    
    public static void highlightIncorrectButton(int randNum, ArrayList<String> incorrectAnswer, int lifelineType){
        if (incorrectAnswer.get(randNum) == "A"){
            QuestionScreen.btnAHighlight=lifelineType; //0 would be no highlight, 1 would be black, 2 would be green
        }
        else if (incorrectAnswer.get(randNum) == "B"){
            QuestionScreen.btnBHighlight = lifelineType;
        }
        else if (incorrectAnswer.get(randNum) == "C"){
            QuestionScreen.btnCHighlight = lifelineType;
        }
        else{
            QuestionScreen.btnDHighlight = lifelineType;
        }
    }
    
    public static void lifeLine(int questionNumber, int lifelineType){
        Random rand = new Random();
        ArrayList<String> incorrectAnswer = new ArrayList<String>();
        switch(questionsMain.get(questionNumber).get(5)){
            case "A":
                incorrectAnswer.add("B");
                incorrectAnswer.add("C");
                incorrectAnswer.add("D");
            case "B":
                incorrectAnswer.add("A");
                incorrectAnswer.add("C");
                incorrectAnswer.add("D");
            case "C":
                incorrectAnswer.add("A");
                incorrectAnswer.add("B");
                incorrectAnswer.add("D");
            case "D":
                incorrectAnswer.add("A");
                incorrectAnswer.add("B");
                incorrectAnswer.add("C");
        }
        
        if(lifelineType == 1){
            
            int  randNum1 = rand.nextInt(3);
            int randNum2 = rand.nextInt(3);
            while (randNum2 == randNum1){
                randNum2 = rand.nextInt(3);     
            }
            highlightIncorrectButton(randNum1, incorrectAnswer, 1);
            highlightIncorrectButton(randNum2, incorrectAnswer, 1);
        }
        else{
            int randNum3 = rand.nextInt(2);
            
            if (randNum3 == 0){ //give user correct answer
                String answer = questionsMain.get(question).get(5);                
                if(answer.equals("A")){
                   QuestionScreen.btnAHighlight = 2; 
                }
                else if (answer.equals("B")){
                    QuestionScreen.btnBHighlight = 2;
                }
                else if (answer.equals("C")){
                    QuestionScreen.btnCHighlight = 2;
                }
                else if (answer.equals("D")){
                    QuestionScreen.btnDHighlight = 2;
                }

            }
            else{
                int  randNum4 = rand.nextInt(3);
                highlightIncorrectButton(randNum4, incorrectAnswer, 2);
            }
        
        }
    }
    
    public static int randomQuestion(){
        Random rand = new Random(); 
        if (questionNumber <=5){
            question = ThreadLocalRandom.current().nextInt(0, (questionsMain.size() - 19));
        }
        else if (questionNumber <= 10 && questionNumber > 5){
            question = ThreadLocalRandom.current().nextInt(4, (questionsMain.size() - 11));
        }
        else{
            question = ThreadLocalRandom.current().nextInt(7, (questionsMain.size()));
        }

        return (question);
    }
    
    public static ArrayList<ArrayList<String>> loadQuestions(){
        int questionNum = 27;

        String fName = "Q&A.txt";
        String line = null;
        
        try{
            FileReader fileReader = new FileReader(fName);
            BufferedReader bufferedReader = new BufferedReader(fileReader); 
            for (int j=0; j<questionNum;j++){
                questionsMain.add(new ArrayList<String>());
                for (int i=0; i<6;i++){
                    line = bufferedReader.readLine();
                    if (line == null){
                        break;
                    }
                    else {
                        questionsMain.get(j).add(i, line);
                    }
                }              
            }
        }
        
        catch(FileNotFoundException ex){
            System.out.println("Cannot find file "+ fName + " .");
        }
        catch(IOException ex){
            System.out.println("Unable to open file '" + fName + "'");
        }

        return(questionsMain);
    }
    
    public static void main(String[] args) {
        StartScreen start = new StartScreen();
        start.setVisible(true);

        loadQuestions();
    }
}
