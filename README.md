# Infograficos de Inteligencia Artificial

Coleção de slides sobre modelos de IA, agentes, orquestração, RAG, MCP,
memórias, segurança e ecossistemas de desenvolvimento.

## Agent Harness

**Slide 1 — Agent Harness:** apresenta o harness como a infraestrutura que transforma um LLM, gerador de texto, em um agente capaz de agir no mundo real.

![Slide 1](<SLIDES/Agent Harness/capa_agente_harness_slide_1-O_LLM_em_Agent.jpeg>)

**Slide 2 — O problema do LLM isolado:** um LLM stateless apenas recebe e devolve texto; não executa código, não mantém memória, não usa ferramentas e não valida resultados.

![Slide 2](<SLIDES/Agent Harness/agente_harness_slide_2_LLM_Stateless.jpeg>)

**Slide 3 — Fórmula do agente:** agente é a combinação de modelo, responsável por raciocínio e linguagem, com harness, responsável por ferramentas, memória, estado, loops e guardrails.

![Slide 3](<SLIDES/Agent Harness/agente_harness_slide_3_A_Formula_Agent_igual_modelo_plus_harness.jpeg>)

**Slide 4 — Ciclo ReAct:** o agente repete as etapas de raciocinar, agir, observar o resultado e continuar até concluir a tarefa.

![Slide 4](<SLIDES/Agent Harness/agente_harness_slide_4_Ciclo_React.jpeg>)

**Slide 5 — Componentes de um harness:** execução de ferramentas, memória entre turnos, gerenciamento de contexto, políticas de permissão com aprovação humana e recuperação de erros.

![Slide 5](<SLIDES/Agent Harness/agente_harness_slide_5_Components_que_Harness_precisa.jpeg>)

**Slide 6 — Harness engineering:** define uma disciplina que trata contexto, ferramentas, memória do projeto, estado, observabilidade e verificação como runtime auditável separado do modelo.

![Slide 6](<SLIDES/Agent Harness/agente_harness_slide_6_Harness_Engineering.jpeg>)

**Slide 7 — Implementações reais:** destaca Claude Agent SDK, LangChain Deep Agents e Microsoft Agent Framework como soluções que dão ao modelo meios de agir, lembrar e verificar.

![Slide 7](<SLIDES/Agent Harness/agente_harness_slide_7_Exemplos_Reais.jpeg>)

**Slide 8 — Stack 2026:** propõe LangGraph, Claude ou GPT, Postgres com pgvector e Redis, E2B Sandbox, MCP, APIs, navegador, Pydantic e LangSmith para agentes prontos para produção.

![Slide 8](<SLIDES/Agent Harness/agente_harness_slide_8_Stack_2026.jpeg>)

## Como LLM Opera

**Slide 1 — Como uma LLM funciona:** resume input, tokenização, embeddings, processamento Transformer, predição do próximo token, sampling e loop autorregressivo que forma a resposta.

![Slide 1](<SLIDES/Como_LLM_Opera/Como_LLM_Opera_Slide1.jpeg>)

## Ecossistema Claude

**Slide 1 — Ecossistema Claude:** introduz capacidades de raciocínio avançado, agentes autônomos e integração multimodal da Anthropic.

![Slide 1](<SLIDES/Ecossistema_Claude/Ecossistema_Claude_Slide1.jpeg>)

**Slide 2 — Recursos do Claude:** apresenta modelos Opus, Sonnet e Haiku, Artifacts e Design, Projects, Claude Code, conectores MCP e recursos inteligentes como visão e thinking.

![Slide 2](<SLIDES/Ecossistema_Claude/Ecossistema_Claude_Slide2.jpeg>)

**Slide 3 — Planos de acesso:** compara os planos Gratuito, Pro e Max quanto a modelos, limites, contexto, projetos, uploads e prioridade de acesso.

![Slide 3](<SLIDES/Ecossistema_Claude/Ecossistema_Claude_Slide3.jpeg>)

## Ecossistemas Agentes IA

**Slide 1 — Ecossistema de agentes:** apresenta a transição do mercado de experimentação para produção de agentes de IA.

![Slide 1](<SLIDES/Ecossistemas_Agentes_IA/Ecossistemas_Agentes_IA_Slide_1.jpeg>)

**Slide 2 — Protocolos:** explica MCP para conexão modelo-ferramenta, A2A para colaboração entre agentes e a convergência para interoperabilidade e governança unificada.

![Slide 2](<SLIDES/Ecossistemas_Agentes_IA/Ecossistemas_Agentes_IA_Slide_2.jpeg>)

**Slide 3 — Frameworks:** lista LangGraph, Microsoft Agent Framework, Claude Agent SDK, OpenAI Agents SDK, Google ADK, CrewAI, LlamaIndex, Pydantic AI, Mastra e AG2.

![Slide 3](<SLIDES/Ecossistemas_Agentes_IA/Ecossistemas_Agentes_IA_Slide_3.jpeg>)

**Slide 4 — Plataformas empresariais:** apresenta pilares de raciocínio e execução, memória e coordenação, além de observabilidade, em plataformas como Copilot Studio, Bedrock, Vertex, Agentforce e watsonx.

![Slide 4](<SLIDES/Ecossistemas_Agentes_IA/Ecossistemas_Agentes_IA_Slide_4.jpeg>)

**Slide 5 — Tendências:** destaca coding agents, hibridização de modelos, interfaces TUI para múltiplos agentes e plugins WASM em sandbox.

![Slide 5](<SLIDES/Ecossistemas_Agentes_IA/Ecossistemas_Agentes_IA_Slide_5.jpeg>)

## Enxames Agentes IA

**Slide 1 — Enxames de agentes:** compara agente individual e swarm, descreve o fluxo Planner, Workers, Verifier e Merge, e relaciona modelos, paralelismo, autonomia e tool calling.

![Slide 1](<SLIDES/Enxames_Agentes_IA/Enxames_Agentes_IA_SWORM_slide-1.jpeg>)

## Glossario Geração Agentes IA

**Slide 1 — Glossário técnico:** reúne termos de configuração e geração de agentes, incluindo LLM, system prompt, user prompt, temperature, top-p/top-k, tokens, embeddings, chunking, planejamento, tool calling, observabilidade e guardrails.

![Slide 1](<SLIDES/Glossario_Geração_Agentes_IA/Glossario_Geração_Agentes_IA_Slide_1.jpeg>)

## Instalação MCP

**Slide 1 — Instalação do MCP:** descreve pré-requisitos, configuração no Claude Desktop e Cursor, MCP CLI, criação de servidor Python, integração de servidores e práticas de produção com Docker e Kubernetes.

![Slide 1](<SLIDES/Instalação_MCP/Instalação_MCP_Slide_1.jpeg>)

**Slide 2 — Código MCP:** mostra exemplos de configuração `mcp.json`, definição de ferramentas em Python e TypeScript, uso por agentes e servidores populares para filesystem, GitHub, banco, Slack, browser, busca e memória.

![Slide 2](<SLIDES/Instalação_MCP/Exemplos_Praticos_Codigo_MCP_Slide1.jpeg>)

## Memorias Agentes IA

**Slide 1 — Memórias de agentes:** diferencia memória de trabalho, curto prazo, implícita e longo prazo para manter continuidade e contexto sob controle do usuário.

![Slide 1](<SLIDES/Memorias_Agentes_IA/Memorias_Agentes_IA_Slde_1.jpeg>)

**Slide 2 — Arquitetura de memória:** apresenta camadas de memória, admissão, recuperação semântica, seleção pelo planejador, execução e evolução, comparando retenção e volatilidade.

![Slide 2](<SLIDES/Memorias_Agentes_IA/Memorias_Agentes_IA_Slde_2.jpeg>)

**Slide 3 — RAG:** explica Retrieval-Augmented Generation como busca vetorial de fontes externas, atualizáveis e verificáveis para responder com contexto em tempo real.

![Slide 3](<SLIDES/Memorias_Agentes_IA/Duas_Formas_de_dar_memorias_para_IA_RAG_e_CAG_Slide1.jpeg>)

**Slide 4 — CAG:** apresenta Cache-Augmented Generation, que pré-carrega conhecimento no cache KV para respostas de baixa latência.

![Slide 4](<SLIDES/Memorias_Agentes_IA/Duas_Formas_de_dar_memorias_para_IA_RAG_e_CAG_Slide2.jpeg>)

**Slide 5 — Escolha entre RAG e CAG:** compara dados dinâmicos e estáveis, escala, velocidade, complexidade e exemplos de uso para decidir a estratégia de memória.

![Slide 5](<SLIDES/Memorias_Agentes_IA/Duas_Formas_de_dar_memorias_para_IA_RAG_e_CAG_Slide3.jpeg>)

**Slide 6 — RAG em Java:** detalha ingestão, chunking, embeddings, busca vetorial e geração com LLM, além de stack com Spring AI ou LangChain4j, banco vetorial e aplicações empresariais.

![Slide 6](<SLIDES/Memorias_Agentes_IA/RAG in JAva.jpeg>)

## Modelos IA Americanos X Chineses

**Slide 1 — Modelos americanos e chineses:** compara recursos de OpenAI, Anthropic, Google e xAI com DeepSeek, Qwen, GLM, Kimi, MiniMax e IQuest, considerando contexto, custo, abertura e cenários de uso.

![Slide 1](<SLIDES/Modelos_IA_AmericanosXChineses/Modelos_IA_AmericanosXChineses_Slide1.jpeg>)

## Modelos IA Open and Closed Source

**Slide 1 — Open source versus closed source:** contrasta modelos abertos e proprietários para código em custo, privacidade, controle, suporte, contexto, segurança e adequação a cenários como startups, enterprise e pesquisa.

![Slide 1](<SLIDES/Modelos_IA_Open&Closed_Source/Modelos_IA_Open&Closed_Source_Slide_1.jpeg>)

**Slide 2 — Comparativo de modelos:** organiza modelos de 11 empresas por especialidade, contexto e custo de tokens, e recomenda opções para código, custo-benefício, contexto longo, autonomia e uso open source.

![Slide 2](<SLIDES/Modelos_IA_Open&Closed_Source/Comparativo_Modelos_de_IA_Slide1.jpeg>)

## Orquestração Multi Agentes

**Slide 1 — Arquiteturas multiagente:** introduz seis arquiteturas para escalar de um agente a centenas de agentes colaborativos.

![Slide 1](<SLIDES/Orquestração_Multi_Agentes/Orquestração_Multi_Agentes_Slide_1.jpeg>)

**Slide 2 — Centralizada ou supervisor:** usa um orquestrador central para alto controle e facilidade de depuração, com possível gargalo para workflows rígidos.

![Slide 2](<SLIDES/Orquestração_Multi_Agentes/Orquestração_Multi_Agentes_Slide_2.jpeg>)

**Slide 3 — Hierárquica:** distribui papéis entre supervisor, gerentes e executores, adequada a organizações e projetos complexos, embora aumente a latência.

![Slide 3](<SLIDES/Orquestração_Multi_Agentes/Orquestração_Multi_Agentes_Slide_3.jpeg>)

**Slide 4 — Sequencial ou pipeline:** organiza coleta, processamento, validação e saída em fluxo linear, simples e previsível para processamento de documentos.

![Slide 4](<SLIDES/Orquestração_Multi_Agentes/Orquestração_Multi_Agentes_Slide_4.jpeg>)

**Slide 5 — Descentralizada ou mesh:** permite comunicação peer-to-peer resiliente e criativa, indicada para debate e brainstorming, mas com maior consumo de tokens.

![Slide 5](<SLIDES/Orquestração_Multi_Agentes/Orquestração_Multi_Agentes_Slide_5.jpeg>)

**Slide 6 — Blackboard ou memória compartilhada:** coordena agentes por um espaço comum de memória, útil para contexto longo e RAG, exigindo controle de concorrência e consistência.

![Slide 6](<SLIDES/Orquestração_Multi_Agentes/Orquestração_Multi_Agentes_Slide_6.jpeg>)

**Slide 7 — Mercado ou leilão:** atribui tarefas por lances e capacidades de agentes, otimizando alocação de recursos com maior complexidade de coordenação.

![Slide 7](<SLIDES/Orquestração_Multi_Agentes/Orquestração_Multi_Agentes_Slide_7.jpeg>)

## Reduzir Alucinações IA

**Slide 1 — Redução de alucinações, fundamentos:** combina RAG, CAG, GraphRAG, tool use e debate Proposer-Critic-Judge, apoiados pelo framework SEIMAD de separação, evidência, verificação, debate, auditabilidade e determinismo.

![Slide 1](<SLIDES/Reduzir_Alucinações-IA/tecnicas_usadas_reduzir_alucinaççoes_Slide_1.jpeg>)

**Slide 2 — Redução de alucinações, correção e governança:** reúne self-reflection, memória persistente, guardrails, observabilidade e human-in-the-loop em um pipeline de geração, verificação, debate e saída confiável.

![Slide 2](<SLIDES/Reduzir_Alucinações-IA/tecnicas_usadas_reduzir_alucinaççoes_Slide_2.jpeg>)

## Rnaking IAs 2026

**Slide 1 — Ranking de IAs 2026:** classifica modelos para código e agentes por benchmarks, contexto e custo de API, destacando IQuest-Coder, GLM, Claude, GPT, Gemini, Kimi, DeepSeek, Qwen, Grok e MiniMax.

![Slide 1](<SLIDES/Rnaking_IAs_2026/Rnaking_IAs_2026_Slide_1.jpeg>)

**Slide 2 — IAs para geração de código:** compara modelos americanos e chineses por origem, abertura, linguagens, foco de uso, benchmarks e capacidade de coding agent.

![Slide 2](<SLIDES/Rnaking_IAs_2026/Comparativo_IAs_Geração_Codigo_Slide_1.jpeg>)

## Skills Modelos IA

**Slide 1 — Skills para modelos de IA:** apresenta skills como capacidades reutilizáveis e instruções especializadas que orientam o agente em tarefas e domínios.

![Slide 1](<SLIDES/Skills_Modelos_IA/SKills_Modelos_de_IA-Slide_1.jpeg>)

**Slide 2 — Aplicação de skills:** ilustra como modelos e agentes combinam skills, ferramentas, contexto e regras para executar fluxos especializados com maior consistência.

![Slide 2](<SLIDES/Skills_Modelos_IA/SKills_Modelos_de_IA-Slide_2.jpeg>)
Infográficos sobre inteligência artificial
