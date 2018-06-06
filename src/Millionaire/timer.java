
package Millionaire;
import static Millionaire.DoYouWantToBeAMillionaire.timerSum;
import static Millionaire.QuestionScreen.timer_end;
import java.awt.Color;
import java.util.concurrent.TimeUnit;
import javax.swing.JOptionPane;


public class timer extends javax.swing.JFrame implements Runnable {
    
    public static int timer = 30;
    
    public void run(){    
            try{
                while(true){
                    if(DoYouWantToBeAMillionaire.timerActive){
                        if (timer == 0){     
                            DoYouWantToBeAMillionaire.timerActive = false;
                            timer_end();
                            QuestionScreen.ButtonA.setBackground(Color.RED);
                            QuestionScreen.ButtonB.setBackground(Color.RED);
                            QuestionScreen.ButtonC.setBackground(Color.RED);
                            QuestionScreen.ButtonD.setBackground(Color.RED);
                            QuestionScreen.btnClicked = true;
                            QuestionScreen.answerCorrect = false;
                            JOptionPane.showMessageDialog(null, "TIMES UP!");
                            break;
                        }
                        else {
                            QuestionScreen.TimeLabel.setText(Integer.toString(timer));
                            Thread.sleep(1000);
                            timer -= 1;
                        }
                    }
                    else{
                        System.out.println(timer + " " + timerSum);
                        timerSum += (30-timer-1);
                        System.out.println(timerSum);
                        break;
                    }  
                }  
            }
            catch(Exception e){
            }
        }    
}
