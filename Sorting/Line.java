/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package Objetos;

import java.util.ArrayList;

/**
 *
 * @author cadu
 */
public class Line {
    private ArrayList<Client> line;
    private int lastPriority = -1;
    
    public Line (){
        this.line = new ArrayList<Client>();
    }
    
    public Line (String name){
        Client newEntry = new Client(name);
        this.line = new ArrayList<Client>();
        line.add(newEntry);
    }
    
    public Line (String name, boolean priority){
        Client newEntry = new Client(name, priority);
        this.line = new ArrayList<Client>();
        this.lastPriority = 0;
        this.line.add(newEntry);
    }
    
    public void addClient(String name){
        Client newEntry = new Client(name);
        this.line.add(newEntry);
    }
    
    public void addPriority(String name){
        Client newEntry = new Client(name);
        this.line.add(this.lastPriority, newEntry);
        this.lastPriority = this.line.lastIndexOf(newEntry);
    }
    
}
