
Templates
###########
    
This document containers the templates available to Janis by default. These are used
to configure Cromwell to execute across a number of compute environments.

Janis can be configured to submit to an existing Cromwell instance (including on GCP) with:

.. code-block:: bash

   urlwithport="127.0.0.1:8000"
   janis run --engine cromwell --cromwell-url $urlwithport hello




List of templates for ``janis-assistant``:

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   local
   pawsey
   pawsey_disconnected
   pbs_singularity
   pmac
   pmac_disconnected
   singularity
   slurm_singularity
   spartan
   spartan_disconnected
   wehi

*This page was auto-generated on 17/01/2020. Please do not directly alter the contents of this page.*
