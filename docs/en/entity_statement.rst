.. include:: ../common/common_definitions.rst

.. _Entity_Statement:

Entity Statements
-----------------

The basic component for building a Trust Chain is the **Entity Statement (ES)**, a signed JWT that
contains the signing keys of the subordinate Entities and further data used to control the
process of Trust Chain resolution.

An Entity publishes an **ES** related to a subordinate, at its :ref:`Fetch Endpoint<Esempio_EN2>`. 
The superior Entity MAY define the Metadata policy of the subordinate subjects 
and publish the TMs that it has issued for them.


Entity Statement Signature
++++++++++++++++++++++++++

The same considerations made for the **ECs** and reported in the section :ref:`Firma della Entity Configuration<firma_EC>`, apply.


Entity Statement
++++++++++++++++

The ES issued by the TA or by an Intermediary for its own direct subordinates, contain also the following
attributes:


.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Description**
     - **Supported by**
   * - **metadata_policy**
     - JSON Object that describes the Metadata policy. Each key of the JSON Object represents an 
       identifier of the type of Metadata and each value MUST be a JSON Object that represents the Metadata 
       policy according to that Metadata type. Please refer to the `OIDC-FED#Section.5.1`_ specifications
       for the implementation details.
     - |spid-icon| |cieid-icon|
   * - **trust_marks**
     - JSON Array containing the Trust Marks issued by itself for the subordinate subject.
     - |spid-icon| |cieid-icon|


.. seealso:: 

   - `OIDC-FED#Section_3.1`_
   - :ref:`Non-normative example of Entity Statement<Esempio_EN2.1>`

