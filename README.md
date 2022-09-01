# TUI for jellyfin browsing

## Launch application

```bash
app/app.py
```

`Ctrl+q` to quit

## Dev

Install dep:

```bash
pipenv shell
pipenv install requests
```

Links:

- https://dev.to/wiseai/textual-the-definitive-guide-part-2-6h8
- https://pypi.org/project/python-mpv/

---

TODO:

- [x] lister les dernière vidéos ajoutées
- [x] clique sur les items pour lire la vidéo avec mpv
- [ ] fermeture clean du player
- [ ] afficher la jaquette
- [ ] sauvegarde continue de l'avancement de la lecture de la vidéo
- [ ] lister en premier les lectures en cours
- [ ] formulaire de recherche de vidéo (Ctrl+s)
- [ ] recherche instantanée
