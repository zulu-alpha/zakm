# Zulu-Alpha Kit Manager

The ZAKM uses a [ZAKI](https://github.com/zulu-alpha/zaki) DB and kit specification YAML file to modify a mission.sqm file, in order to load out units and crates and also to generate an accompanying human readable document.

This allows there to be one **Source of Truth** file for all kit available to specific groups and roles in a mission. This source of truth file is used to do the actual kitting out of the mission file and generation of a document for WARNORDs or other mission related documents, all with a single action, thus minimizing the work that needs to be done and minimizing the chance for discrepencies between documentation and actually available kit. The ZAKM thus enables the principle of **DRY** (**D**on't **R**epear **Y**ourself) for your kit.

This file also allows different kit to be loaded depending on different conditions, such as terrain conditions and mission type, thus maximizing the re-use of the specification file.

## Kit specification file

All kit for all units and crates and the generated human readable documents are derived from kit specification files written in YAML. If you would like to learn only what you need to edit the kit specification file, then please see the [Quick Yaml Intro](https://github.com/zulu-alpha/zakm/blob/master/quick-yaml-intro.md).

All the keys in the kit specification files have special meaning and their level in the document hierarchy is important.

### Structure

On the top level of the document, there are specifications for visibility and terrain conditions (more on those under the heading **Kit object conditions**), universal kit collections (more on kit collections under the heading **Kit collections**), universal crate cargo (more on crate cargo under the heading **Kit containers**) and finally the object **Group types**.

**Group types** is an object that holds an array of all of the different group type objects and their corresponding units (represented by **roles**) that will be equipped. An important thing to note is that several different groups that need to be kitted out the exact same way can all be dealt with in the same group type object.

A group type object has several keys:

* `title`
  * A short word or phrase describing the group (eg: `Rifle Squad`)
* `description` (Optional)
  * A longer description

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
* `miscellaneous`
* `muzzle_attachments`
* `nvgs`
* `optic_attachments`
* `primary_weapons`
* `secondary_weapons`
* `side_attachments`
* `sidearms`
* `uniforms`
* `vests`
* `watches`

## equippable kit

Kit can be equipped directly to a person, via their role.
This is done by simply putting a kit object and it's category in the `on_person` object of that role.
For example, to equip a uniform to a role:

```yaml
on_person:
  uniforms:
    - type: za_fat1_soldier_arid
```

Note that the kit object is part of an array. This is because the ZAKM allows different equippable kit to be equipped depending on different conditions.
For example, to equip a different uniform depending terrain conditions, you would write it like so:

```yaml
on_person:
  uniforms:
    - type: za_fat1_soldier_arid
      terrain_conditions:
        - Arid
    - type: za_fat1_soldier_trans
      terrain_conditions:
        - Transitional
```

More on conditions later, under the heading **Kit object conditions**.

Note that when actually using a specification file to kit out units in a mission.sqm, once all conditions are determined (such as terrain conditions in this example), then only one kit object for each category must remain, otherwise an error will be thrown, as only one kit object for each kit category can be equipped at a time.

All of the possible equippable kit categories and how to write them are:

* `backpacks`
* `binoculars`
* `compasses`
* `goggles`
* `headgear`
* `interfaces`
* `maps`
* `nvgs`
* `primary_weapons`
* `secondary_weapons`
* `sidearms`
* `uniforms`
* `vests`
* `watches`

### Kit for equippable kit

Certain equippable kit categories can have their own kit such as weapon attachments and magazines. These are:

* `binoculars`
* `primary_weapons`
* `secondary_weapons`
* `sidearms`

To actually equip kit to those categories, you use these keys:

* `on_binoculars`
* `on_primary_weapon`
* `on_secondary_weapon`
* `on_sidearm`

The kit categories that you can equip to those kit categories are:

* `bipod_attachments`
* `muzzle_attachments`
* `optic_attachments`
* `side_attachments`
* `magazines`

However, there can be two different muzzles (for example a rifle with an underslung grenade launcher), so `magazines` needs to be contained in one of two special keys, namely:

* `primary_muzzle_magazines`
* `secondary_muzzle_magazines`

To put all of this together with an example:

```yaml
on_person:
  primary_weapons:
    - type: arifle_SPAR_01_GL_blk_F
  on_primary_weapon:
    bipod_attachments:
      - type: bipod_01_F_blk
    muzzle_attachments:
      - type: muzzle_snds_M
    optic_attachments:
      - type: optic_Holosight_blk_F
    side_attachments:
      - type: acc_pointer_IR
    primary_muzzle_magazines:
      magazines:
        - type: 30Rnd_556x45_Stanag
    secondary_muzzle_magazines:
      magazines:
        - type: 1Rnd_HE_Grenade_shell
```

Please note that the rifle in the above example can't actually have a bipod, but for illustrative purposes, one was added anyway.

Also please note that at this time, the ZAKM does not validate that a compatible attachment or magazine is used for a given weapon or binocular. Using an incompatible kit will break the game in strange ways, so please make sure that you use the right ones.

## Kit containers

A kit container is just an object that can end up containing any number of any category of kit, and there are 4 kinds of kit containers.

There are crate containers, for example:

```yaml
crate_cargo:
  - crate: Main
    binoculars:
      - type: ACE_Vector
    interfaces:
      - type: ItemAndroid
  - crate: Medical
    miscellaneous:
      - type: ACE_elasticBandage
        count: 5
      - type: ACE_packingBandage
        count: 5
```

Each crate has a name (for e.g: `Main` and `Medical`) and are elements in an array that belongs to the `crate_cargo` object.
Crate cargo can be in the scope of a group, or at the top level of the document, which can be shared among all groups.

The other containers are on an actual person, in the `on_person` object. There are 3 and each of them and how they are written are as follow:

* `uniform_cargo`
* `vest_cargo`
* `backpack_cargo`

An example of how to use them is as follows:

```yaml
on_person:
  uniform_cargo:
    miscellaneous:
      - type: ACE_elasticBandage
        count: 5
      - type: ACE_packingBandage
        count: 5
  vest_cargo:
    grenades:
      - type: HandGrenade
        count: 4
      - type: ACE_M84
        count: 2
  backpack_cargo:
    grenades:
      - type: SmokeShellBlue
        count: 2
      - type: SmokeShellRed
        count: 2
```

You would of course also need to specify a uniform, vest and backpack to contain those kit objects in the given example.

## Kit object conditions

You can set a condition for a particular kit object, so that it only gets applied when certain conditions are met and the ZAKM auto-documentation feature will also let the reader know under which conditions the kit is intended to be used.

There are 4 types of conditions. The are no hard coded conditions for any of the condition types, as they are all user defined in the specification file.
The ZAKM will detect which conditions are available in the file and ask which ones to use when the ZAKM applied on a mission.sqm.

The 4 types of kit conditions and how they are written are:

* `visibility_conditions`
* `terrain_conditions`
* `group_conditions`
* `role_conditions`

More on exactly what they are and where to define them under the *Condition definitions* heading later on.

Each condition type can have any number of conditions, which are just user defined strings in an array.

To add a condition to a kit object, you simply add the condition type key that the condition belongs to in the kit object and specify all the conditions that the kit should be applied for. For example:

```yaml
type: za_fat1_soldier_trans
  terrain_conditions:
    - Transitional
    - Woodland
```

Notice that the two conditions, `Transitional` and `Woodland`. This allows you to for example have a certain item of clothing applied for both Transitional and Woodland terrain conditions.

You can also have as many of the 4 condition types at the same time, such as in this example:

```yaml
- type: CUP_NVG_GPNVG_tan
  visibility_conditions:
    - Night
  terrain_conditions:
    - Arid
```

Here, these particular Tan coloured NVGs are only used when it is both night and arid.

### Condition definitions

Each condition is defined by a condition object, which is basically just this key value pair:

```yaml
- name: <Some condition name>
```

The exception to this is with Terrain conditions, where they will also have a `worlds` attribute. Examples will be given below.

Notice as well that the above object is an element in an array, as you will necessarily want to implement several conditions for each condition type.

The 4 condition types are:

#### Visibility conditions

Examples are day or night. Other conditions such as heavy fog could also be added here.
This is a top level condition that is shared across all groups and roles.

This is defined at the top level of the specification file (not inside anything like a group).

For example:

```yaml
visibility_conditions:
  - name: Night
  - name: Day
```

#### Terrain conditions

Examples are Arid, Transitional or Woodland. Other terrain conditions could be added such as Snow.
This is also a top level condition that is shared across all groups and roles.

This is also defined at the top level of the specification file (not inside anything like a group).

This condition type is different from the others due to the *worlds* key, which allows the ZAKM to automatically detect which terrain the mission.sqm belongs to and choose the right terrain condition for you.
The corresponding value is an array of strings.

```yaml
name: <Some condition name>
worlds:
  - <Some terrain name>
  - <Some terrain name>
```

Where `<Some terrain name>` is the [world name](https://community.bistudio.com/wiki/worldName) of the terrain and there can be as many of them as you like.

For example:

```yaml
terrain_conditions:
  - name: Arid
    worlds:
      - takistan
      - zargabad
  - name: Transitional
    worlds:
      - altis
      - malden
      - stratis
  - name: Woodland
    worlds:
      - chernarus
      - tanoa
```

#### Group conditions

Examples are CQC or Long Range. There are many other possibilities here depending on the groups mission and situation.
This is a group level condition defined inside the scope of a group that is shared across all roles in the same group.

For example:

```yaml
group_conditions:
  - name: CQC
  - name: Long Range
  - name: Wetworks
```

#### Role conditions

Examples are Ammo Bearer or Laser Designator, along with many other possibilities.
This is a condition that is defined inside of a role and which only effects that particular role.

```yaml
role_conditions:
  - name: Long range communication
  - name: Laser designator
```

## Kit collections
