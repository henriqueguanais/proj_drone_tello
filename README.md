# **Logística Autônoma em Ambientes Fechados com Drones DJI Tello**  
## Participantes
- [Helton Maia](https://heltonmaia.com/) (professor)
- [Bruno Marques](https://sigaa.ufrn.br/sigaa/public/docente/portal.jsf?siape=1170845) (professor)
- Murilo de Lima Barros (aluno)

## **Descrição do Projeto**  
Este projeto desenvolve um sistema de logística autônoma em ambientes fechados utilizando drones DJI Tello equipados com câmeras para identificar e navegar até QR codes. Nossa solução busca otimizar tarefas de transporte de pequenos itens, monitoramento e inventário em escritórios, galpões e hospitais, oferecendo eficiência, flexibilidade e baixo custo.

## **Novas Funcionalidades de Chatbot e Controle**
- **Chatbot Integrado:** permite interação natural (texto) com o sistema via interface Streamlit. O usuário digita comandos livres, o chatbot interpreta e gera o comando DJI Tello correspondente.
- **Processamento de Comandos:** uso de `process_ai_command` para validar e enfileirar instruções recebidas do chatbot, com feedback em tempo real no histórico de chat.
- **Interface Streamlit:** painel web para:
  - Visualizar vídeo ao vivo do drone
  - Enviar comandos manuais e via chatbot
  - Exibir parâmetros de voo (bateria, altura, pressão, temperatura, tempo e FPS)
  - Logs de comandos e chat

## **Principais Funcionalidades em Desenvolvimento**
- **Detecção de QR Codes:** OpenCV + PyZbar para leitura em tempo real.
- **Chatbot-AI:** interpretação de linguagem natural para comandos do drone (por ex. “siga”, “pouse quando chegar”, “voe 50 cm para frente”).

## **Ferramentas Utilizadas**
- **Hardware:** Drone DJI Tello
- **Software:** Python, OpenCV, PyTello SDK, PyZbar, Streamlit
- **IA & NLP:** Chatbot baseado em modelo de linguagem (Gemini)

## **Status Atual**
- Streaming de vídeo e telemetria funcionando
- Integração do chatbot e fila de comandos
- Movimentação básica e follow via QR code implementados

## **Instalação**
```bash
# Clone o repositório
git clone https://github.com/heltonmaia/proj_drone_tello.git
cd proj_drone_tello
```
```bash
# Instale dependências
sudo apt-get install portaudio19-dev
pip install -r requirements.txt
```  

```bash
# Instale o modelo de reconhecimento de áudio
cd models
wget https://alphacephei.com/vosk/models/vosk-model-pt-fb-v0.1.1-20220516_2113.zip
unzip vosk-model-pt-fb-v0.1.1-20220516_2113.zip
```  

## **Uso**
1. **Conecte-se** à rede Wi‑Fi do drone DJI Tello.
2. **Execute** a interface Streamlit:
   ```bash
   streamlit run main.py
   ```
3. **Na UI**:
   - Visualize o vídeo ao vivo.
   - Digite um comando manual ou conversacional na caixa de texto.
   - Veja o histórico de chat e logs de comandos.
   - Ajuste o passo (cm) para movimentos com QR code.
   - Clique em Decolar, Pousar ou Encerrar Drone.

## **Comandos Válidos via Chatbot**
| Comando (palavras livres)      | Ação DJI Tello                      |
|--------------------------------|-------------------------------------|
| “decolar”                      | `takeoff`                           |
| “pousar”                       | `land`                              |
| “suba 30cm”                    | `up 30`                             |
| “desça 20cm”                   | `down 20`                           |
| “vá para frente 50”            | `forward 50`                        |
| “move para a direita 20”       | `right 20`                          |


## **Exemplo de Uso**
![Demonstração](video.gif)


