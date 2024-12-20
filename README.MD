# 1. Configuração Inicial

## git config

Este comando é utilizado para configurar as informações do usuário, como o nome e o e-mail, que serão associados aos commits.

Exemplo:

```git
git config --global user.name "Seu Nome"

git config --global user.email "seuemail@exemplo.com"
```

# 2. Criar um Novo Repositório

## git init

O comando git init é utilizado para iniciar um novo repositório Git em um diretório existente.

Exemplo:
```git
mkdir meu_projeto
```
```git
cd meu_projeto
```
```git
git init
```


# 3. Clonar um Repositório

## git clone

Clonar um repositório significa copiar um repositório remoto para o seu computador.

Exemplo:

```git
git clone https://github.com/usuario/projeto.git
```


# 4. Status do Repositório

## git status

Exibe o estado atual do seu repositório, mostrando alterações nos arquivos, se estão sendo rastreados ou não, e o que está pronto para ser commitado.

Exemplo:

```git
git status
```


# 5. Adicionar Arquivos ao Índice

## git add

Adiciona arquivos ao "staging area", que é uma área temporária onde as mudanças ficam aguardando para serem commitadas.

Exemplo:

```git
git add arquivo.txt
```
```git
git add . (para adicionar todos os arquivos)
```


# 6. Fazer um Commit

## git commit

O git commit grava as mudanças feitas nos arquivos que foram adicionados ao staging area.

Exemplo:

```git
git commit -m "Mensagem do commit"
```


# 7. Ver Histórico de Commits

## git log

Exibe o histórico de commits no repositório.

Exemplo:

```git
git log
```
```git
git log --online
```


# 8. Enviar Alterações para o Repositório Remoto

## git push

Após fazer commits, você precisa enviar as alterações para um repositório remoto (como o GitHub).

Exemplo:

```git
git push origin master
```


# 9. Atualizar o Repositório Local com Alterações Remotas

## git pull

Atualiza seu repositório local com as últimas mudanças do repositório remoto.

Exemplo:

```git
git pull origin master
```

# 10. Criar e Mudar de Branch

## git branch

Permite listar, criar ou deletar branches. Um branch é uma linha separada de desenvolvimento.

Exemplo:
```git
git branch
```
```git
git branch nova-feature
```
```git
git checkout
```

Troca para outra branch.

Exemplo:

```git
git checkout nova-feature
```
```git
git checkout -b nova-feature (cria uma nova branch e já muda para ela)
```


# 11. Mesclar Branches

## git merge

Une o conteúdo de uma branch com outra.

Exemplo:

```git
git checkout master
```
```git
git merge nova-feature
```


# 12. Descartar Mudanças

## git checkout -- <arquivo>

Descarta mudanças locais em um arquivo que ainda não foi adicionado ao staging area.

Exemplo:

```git
git checkout -- arquivo.txt
```
```git
git reset
```
Remove arquivos do staging area.

Exemplo:

```git
git reset arquivo.txt
```
```git
git reset --hard (descarta todas as mudanças locais)
```


# 13. Fork e Pull Request no GitHub

- Quando trabalhamos em projetos open source no GitHub, é comum utilizarmos o conceito de fork e pull request.

## Fork

Um fork é uma cópia de um repositório que permite que você faça alterações sem afetar o projeto original.

Exemplo de como fazer fork:

No GitHub, vá até o repositório desejado e clique no botão "Fork". Isso criará uma cópia do repositório no seu perfil.

## Pull Request

Após fazer um fork e realizar alterações, você pode abrir um pull request para sugerir que suas mudanças sejam incorporadas no repositório original.

Exemplo:

- Faça um commit das suas alterações e envie para o seu repositório forkado no GitHub com git push.

- Vá até o repositório original no GitHub e clique em "New Pull Request".

- Descreva suas alterações e submeta o pull request.
