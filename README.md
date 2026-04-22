# 🛡️ SOC Threat Intelligence Dashboard (Blue Team Operations)

Este projeto simula uma operação real de um **Security Operations Center (SOC)**, transformando logs brutos de um SIEM em inteligência defensiva. O foco é identificar padrões de ataque, monitorar a eficiência das regras de firewall e priorizar a resposta a incidentes críticos.

## 🎯 O Desafio de Segurança
Em um ambiente corporativo, milhares de alertas são gerados por segundo. O "ruído" dificulta a identificação de ameaças reais. Este dashboard foi construído para que o time de **Blue Team** consiga visualizar em tempo real (janela de 24h) tentativas de **SQL Injection**, **Brute Force** e **Malwares**, permitindo uma resposta coordenada.

## 🛠️ Stack Tecnológica & Boas Práticas
* **Python (Pandas/Numpy):** Simulação de 5.000 logs de segurança com geolocalização de IP.
* **MySQL Data Warehouse:** Modelagem em **Star Schema** para alta performance em grandes volumes de logs.
* **DevSecOps:** Implementação de segurança de credenciais via variáveis de ambiente (`.env`), garantindo que senhas de banco de dados nunca sejam expostas no código.
* **Power BI & DAX Avançado:** Desenvolvimento de métricas de eficiência de bloqueio e análise de tendências temporais.

## 📊 KPIs de Inteligência Defensiva
1. **Taxa de Eficiência de Bloqueio:** Monitoramento percentual de ameaças neutralizadas automaticamente pelo Firewall.
2. **Análise de Fingerprinting:** Identificação automática da vulnerabilidade mais explorada no período (ex: foco em ataques de injeção de SQL).
3. **Heatmap de Ameaças Globais:** Visualização geográfica de IPs atacantes para suporte a regras de Geo-Blocking.
4. **Status de Risco Dinâmico:** Algoritmo DAX que define o nível de alerta da infraestrutura (Emergência, Alerta ou Seguro) com base na severidade dos incidentes.

## 🎨 Interface & UX (Dark SOC Style)
O design foi construído seguindo os princípios de **Glassmorphism** e **Dark Mode**, utilizando efeitos de brilho neon para destacar métricas críticas. O contraste proposital facilita a leitura em ambientes de monitoramento 24/7.

---
**Nota Técnica:** Este é um projeto de portfólio para demonstração de competências em Análise de Dados e Cibersegurança. Todos os IPs e logs são fictícios, gerados via script Python.
