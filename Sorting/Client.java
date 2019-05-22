/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package Objetos;

/**
 *
 * @author cadu
 */
public class Client {
    private String name;
    private boolean preferential;
    
    public Client(String name){
        this.name = name;
        this.preferential = false;
    }
    
    public Client (String name, boolean preferential){
        this.name = name;
        this.preferential = preferential;
    }
    
    public String toString(){
        String aux;
        if(this.preferential){
            aux = ("Cliente: "+this.name+" Preferencial: SIM");
        }
        else{
            aux = ("Cliente: "+this.name+" Preferencial: NAO");
        }
        
        return aux;
    }
}
