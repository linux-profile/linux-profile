This is the point where the information that is added via the command line is stored.
Basically the data is saved in a `.json` file on your machine, without this location:

<details>
    <summary>View path</summary>

<br>

Latest versions, use like this::

```bash
cat ~/.config/linuxp/profile/linux_profile.json > ~/backup_profile.json
```

If you have a version equal to or lower than 1.0.12, use it like this:

```bash
cat ~/.config/linuxp/linux_profile.json > ~/backup_profile.json
```

</details>

## Exemple File

You can find an example profile file from the link below:

<details>
    <summary>View file</summary>

```
curl https://linuxprofile.com/linux_profile.json --output ~/linux_profile.json
```

</details>
