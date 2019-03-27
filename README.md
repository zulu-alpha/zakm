# Zulu-Alpha Kit Manager

Uses a [ZAKI](https://github.com/zulu-alpha/zaki) DB and kit specification YAML files to modify mission.sqm files to load out units and crates accordingly and generate am accompanying human readable document.

## Kit specification file

All kit for all units and crates and the generated human readable documents are derived from kit specification files written in YAML. If you would like to learn only what you need to edit the kit specification file, then pelase see the [Quick Yaml Intro](https://github.com/zulu-alpha/zakm/blob/master/quick-yaml-intro.md)

All the keys in the kit specification files have special meaning and their level in the document hirearchy is important.

## Kit objects

Any item of kit (such as weapons, magazines, radios, uniforms, backpacks, etc.) is represented at it's simplest by a **Kit object** like so:

```yaml
<category>:
  - type: <class name>
    count: <negative or positive number>
```

The `<category>` is the category name as seen in the [ZAKI](https://github.com/zulu-alpha/zaki) DB for the kit but in lower case, so for example, `Primary_Weapons` from the DB will be `primary_weapons` when written in the kit specification file.

`<class name>` is the class name for the item as found in the [ZAKI](https://github.com/zulu-alpha/zaki) DB.
In this example from the DB, the class name is `hgun_P07_F`:

```json
"hgun_P07_F": {
    "description": "Handgun Caliber: 9x21 mm",
    "display_name": "P99"
}
```

`<negative or positive number>` is the total number of the item to add. It can be negative, so that that item can be removed. This is useful for conditional kit, where you may want more kit in certain conditions and less or none of that same kit in other conditions. Conditions will be discussed later.

The `count` key is actually optional when you only want only one of the given item. So if for example, you only want one P99 pistol, you can write the kit object like so:

```yaml
sidearms:
  - type: hgun_P07_F
```

Notice how all the keys of a kit object (`type` and `count` in the examples above) are one element in an array. This is because when you are adding multiple items of the same category to the same person, crate or kit collection (this will also be discussed later on what that is), each kit object is grouped together under the same category name.

So if you where adding two different types of magazines for example, each with their own amount to the same container, you would then write them like this:

```yaml
magazines:
  - type: SMA_30Rnd_556x45_M855A1
    count: 8
  - type: SMA_30Rnd_556x45_M855A1_Tracer
    count: 2
```

### Valid categories

Simply lowercase versions of what is found in the [ZAKI](https://github.com/zulu-alpha/zaki) DB

* `backpacks`
* `binoculars`
* `bipod_attachments`
* `compasses`
* `explosives`
* `goggles`
* `grenades`
* `headgear`
* `interfaces`
* `magazines`
* `maps`
* `miscelaneous`
* `muzzle_attachments`
* `nvgs`
* `optic_attachments`
* `primary_weapons`
* `secondary_weapons`
* `side_attachemnts`
* `sidearms`
* `uniforms`
* `vests`
* `watches`

## Kit object conditions

