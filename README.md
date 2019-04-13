# Load Balancing between Servers using communication Rest
 software that counts words

•	Ideia Geral: Implementar um SD com balanceamento de carga do tipo dinâmico. <br>
•	Requisito Funcional do Sistema: Software de CONTA PALAVRAS. Deve ser um texto grande que requer alto processamento. <br>
•	Recursos Físicos: Smartphone, computador 01, computador 02, computador 03.  <br>
•	Arquitetura: O smartphone é um cliente que está conectado ao computador 01 (middleware), que por sua vez está conectado a dois servidores (computador 02 e 03). <br>
•	Modo de Demostração: O cliente requisita um serviço e o middleware encaminha a requisição a um dos servidores baseando-se na disponibilidade e no nível de consumo de CPU. O resultado é retornado para o cliente pelo middleware. <br>
•	Comunicação: Os serviços nos servidores serão providos por uma interface REST <br>
