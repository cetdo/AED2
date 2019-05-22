/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package Execucao;
import Objetos.Client;
/**
 *
 * @author cadu
 */
public class Execucao {
    public static void main(String[] args) {
        System.out.println("Olá mundo!");
        Client teste = new Client("Carlos");
        System.out.println(teste.toString());
    }
}
