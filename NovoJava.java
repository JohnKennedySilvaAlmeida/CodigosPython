import java.util.*;
public class entraddados {
      public static void main (String[] args){ 

            String nome;
            int idade;
            float altura;
            Scanner entrada = new Scanner (System.in);
            System.out.print("Digite seu nome:");
            nome = entrada.nextLine();
            System.out.print("Digite sua idade:");
            idade = entrada.nextlInt();
            System.out.print("Digite sua altura:");
            altura = entrada.nextFloat();
            entrada.close();

            System.out.println("\nMostrandos os dados:\n");
            System.out.println("Seu nome:"+ nome);
            System.out.println("Sua idade:"+ idade);
            System.out.println("Seu nome:"+ altura);

    }
}    