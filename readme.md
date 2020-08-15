# Domains Diff

- Check new domains in registro.br list https://registro.br/dominio/processo-de-liberacao/

# Usage

```
./main.py lists/lista-processo-liberacao.2020.7.txt lists/lista-processo-liberacao.2020.8.txt
```

## Tips

You can combine the output with FZF

```
./main.py old.txt new.txt | fzf
```

## License

Released under [MIT License](LICENSE)
