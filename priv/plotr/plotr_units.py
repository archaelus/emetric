
def _bytes_kb(b): return b/1024.0 if b != 0 else return 0
def _words_kb(w): return _bytes_kb(w*8.0)

class Units:
    def info(self,key):
        if key in self.units:
            return self.units[key]
        else:
            return {"unit":None,"convert":None,"label":key}
    def __init__(self):

        self.units = {
            "ejd_tick":{"unit":None,"convert":None,"label":"Tick"},
            "ejd_hosts_global_now":{"unit":None,"convert":None,"label":"Time"},
            "ejd_hosts_global_sessions":{"unit":None,"convert":None,"label":"Global Ejabberd Sessions"},
            "ejd_hosts_vsvoasrqsd01.voalte.net_users_total":{"unit":None,"convert":None,"label":"vsvoasrqsd01.voalte.net Total Users"},
            "ejd_hosts_vsvoasrqsd01.voalte.net_users_online":{"unit":None,"convert":None,"label":"vsvoasrqsd01.voalte.net Online Users"},
            "sys_tick":{"unit":None,"convert":None,"label":"Tick"},
            "sys_node":{"unit":None,"convert":None,"label":"Node"},
            "sys_total_ram":{"unit":"KB","convert":_bytes_kb,"label":"Total RAM"},
            "sys_cores":{"unit":None,"convert":None,"label":"Number of CPU cores"},
            "sys_now":{"unit":None,"convert":None,"label":"Time"},
            "sys_procs":{"unit":None,"convert":None,"label":"Erlang Process Count" },
            "sys_context_switches":{"unit":None,"convert":None,"label":"Erlang Context Switches" },
            "sys_gcs":{"unit":None,"convert":None,"label":"Number of Garbage Collextion Runs"},
            "sys_gc_reclaimed":{"unit":"KB","convert":_words_kb,"label":"Words reclaimed"},
            "sys_io_in":{"unit":"KB","convert":_bytes_kb,"label":"Port Input"},
            "sys_io_out":{"unit":"KB","convert":_bytes_kb,"label":"Port Output"},
            "sys_reductions":{"unit":None,"convert":None,"label":"Total Reductions"},
            "sys_reducts_since":{"unit":None,"convert":None,"label":"Reductions Since"},
            "sys_run_queue":{"unit":None,"convert":None,"label":"Process Read to Run (run queue)"},
            "sys_total":{"unit":"KB","convert":_words_kb,"label":"Total Memory Alloc"},
            "sys_processes":{"unit":"KB","convert":_words_kb,"label":"Memory Alloc'd by Erlang Processes"},
            "sys_processes_used":{"unit":"KB","convert":_words_kb,"label":"Memory Used by Erlang Processes"},
            "sys_system":{"unit":"KB","convert":_words_kb,"label":"Memory Alloc by Erlang Emulator"},
            "sys_atom":{"unit":"KB","convert":_words_kb,"label":"Memory Alloc for Erlang Atoms"},
            "sys_atom_used":{"unit":"KB","convert":_words_kb,"label":"Memory Used by Erlang Atoms"},
            "sys_binary":{"unit":"KB","convert":_words_kb,"label":"Memory Alloc'd for Erlang Binary"},
            "sys_code":{"unit":"KB","convert":_words_kb,"label":"Memory Alloc'd for Erlang Code"},
            "sys_ets":{"unit":"KB","convert":_words_kb,"label":"Memory Alloc'd for erts"},
            "sys_user":{"unit":"second","convert":None,"label":"CPU User Time"},
            "sys_nice":{"unit":"second","convert":None,"label":"CPU Nice Time"},
            "sys_kernel":{"unit":"second","convert":None,"label":"CPU Kernel Time"},
            "sys_idle":{"unit":"second","convert":None,"label":"CPU Idle Time"},
            "sys_iowait":{"unit":"second","convert":None,"label":"CPU iowait"},
            "sys_beam_user":{"unit":"second","convert":None,"label":"BEAM User Time"},
            "sys_beam_kernel":{"unit":"second","convert":None,"label":"BEAM Kernel Time"},
            "sys_beam_vss":{"unit":"KB","convert":_bytes_kb,"label":"BEAM vss"},
            "sys_beam_rss":{"unit":"KB","convert":_bytes_kb,"label":"BEAM rss"},
            "sys_beam_minflt":{"unit":None,"convert":None,"label":"Minor Faults/sec"},
            "sys_beam_majflt":{"unit":None,"convert":None,"label":"Major Faults/sec"},
            "sys_mem_total":{"unit":"KB","convert":_bytes_kb,"label":"Total Memory"},
            "sys_mem_free":{"unit":"KB","convert":_bytes_kb,"label":"Memory Free"},
            "sys_buffers":{"unit":"KB","convert":_bytes_kb,"label":"File Buffers"},
            "sys_cached":{"unit":"KB","convert":_bytes_kb,"label":"Page Cache"},
            "sys_swap_cached":{"unit":"KB","convert":_bytes_kb,"label":"Swap Cache"},
            "sys_active":{"unit":"KB","convert":_bytes_kb,"label":"Active Page Cache"},
            "sys_inactive":{"unit":"KB","convert":_bytes_kb,"label":"Inactive Page Cache"},
            "sys_high_total":{"unit":"KB","convert":_bytes_kb,"label":"Memory High Total"},
            "sys_high_free":{"unit":"KB","convert":_bytes_kb,"label":"Memory High Free"},
            "sys_low_total":{"unit":"KB","convert":_bytes_kb,"label":"Memory Low Total"},
            "sys_low_free":{"unit":"KB","convert":_bytes_kb,"label":"Memory Low Free"},
            "sys_swap_total":{"unit":"KB","convert":_bytes_kb,"label":"Swap Total"},
            "sys_swap_free":{"unit":"KB","convert":_bytes_kb,"label":"Swap Free"},
            "sys_dirty":{"unit":"KB","convert":_bytes_kb,"label":"Memory Dirty"},
            "sys_write_back":{"unit":"KB","convert":_bytes_kb,"label":"Memory Write Back"},
            "sys_anon_pages":{"unit":"KB","convert":_bytes_kb,"label":"Memory Anon Pages"},
            "sys_mapped":{"unit":"KB","convert":_bytes_kb,"label":"Memory Mapped"},
            "sys_slab":{"unit":"KB","convert":_bytes_kb,"label":"Memory SLAB"},
            "sys_page_tables":{"unit":"KB","convert":_bytes_kb,"label":"Memory Page Tables"},
            "sys_nfs_unstable":{"unit":"KB","convert":_bytes_kb,"label":"Memory NFS Unstable"},
            "sys_bounce":{"unit":"KB","convert":_bytes_kb,"label":"Memory Bounce"},
            "sys_commit_limit":{"unit":"KB","convert":_bytes_kb,"label":"Memory Commit Limit"},
            "sys_committed_as":{"unit":"KB","convert":_bytes_kb,"label":"Memory Commit AS"},
            "sys_vmalloc_total":{"unit":"KB","convert":_bytes_kb,"label":"Memory vmalloc Total"},
            "sys_vmalloc_used":{"unit":"KB","convert":_bytes_kb,"label":"Memory vmalloc Used"},
            "sys_vmalloc_chunk":{"unit":"KB","convert":_bytes_kb,"label":"Memory vmalloc Chunk"},
            "sys_hugepagesize":{"unit":"KB","convert":_bytes_kb,"label":"Memory Huge Page Size"},
            "sys_lo_recv_bytes":{"unit":"KB","convert":_bytes_kb,"label":"Net lo recv"},
            "sys_lo_recv_packets":{"unit":"KB","convert":_bytes_kb,"label":"Net lo recv packets"},
            "sys_lo_recv_errs":{"unit":None,"convert":None,"label":"Net lo recv errors"},
            "sys_lo_recv_drop":{"unit":None,"convert":None,"label":"Net lo recv drop errors"},
            "sys_lo_recv_fifo":{"unit":None,"convert":None,"label":"Net lo recv fifo errors"},
            "sys_lo_recv_frame":{"unit":None,"convert":None,"label":"Net lo recv frame errors"},
            "sys_lo_recv_compressed":{"unit":None,"convert":None,"label":"Net lo recv compressed packets"},
            "sys_lo_recv_multicast":{"unit":None,"convert":None,"label":"Net lo recv multicast frames"},
            "sys_lo_trans_bytes":{"unit":"KB","convert":_bytes_kb,"label":"Net lo trans"},
            "sys_lo_trans_packets":{"unit":None,"convert":None,"label":"Net lo trans packets"},
            "sys_lo_trans_errs":{"unit":None,"convert":None,"label":"Net lo trans errors"},
            "sys_lo_trans_drop":{"unit":None,"convert":None,"label":"Net lo trans drop errors"},
            "sys_lo_trans_fifo":{"unit":None,"convert":None,"label":"Net lo trans fifo errors"},
            "sys_lo_trans_colls":{"unit":None,"convert":None,"label":"Net lo trans collisions"},
            "sys_lo_trans_carrier":{"unit":None,"convert":None,"label":"Net lo trans carrier errors"},
            "sys_lo_trans_compressed":{"unit":None,"convert":None,"label":"Net lo trans compressed packets"},
            "sys_eth0_recv_bytes":{"unit":"KB","convert":_bytes_kb,"label":"Net eth0 recv"},
            "sys_eth0_recv_packets":{"unit":None,"convert":None,"label":None},
            "sys_eth0_recv_errs":{"unit":None,"convert":None,"label":None},
            "sys_eth0_recv_drop":{"unit":None,"convert":None,"label":None},
            "sys_eth0_recv_fifo":{"unit":None,"convert":None,"label":None},
            "sys_eth0_recv_frame":{"unit":None,"convert":None,"label":None},
            "sys_eth0_recv_compressed":{"unit":None,"convert":None,"label":None},
            "sys_eth0_recv_multicast":{"unit":None,"convert":None,"label":None},
            "sys_eth0_trans_bytes":{"unit":"KB","convert":_bytes_kb,"label":"Net eth0 trans"},
            "sys_eth0_trans_packets":{"unit":None,"convert":None,"label":None},
            "sys_eth0_trans_errs":{"unit":None,"convert":None,"label":None},
            "sys_eth0_trans_drop":{"unit":None,"convert":None,"label":None},
            "sys_eth0_trans_fifo":{"unit":None,"convert":None,"label":None},
            "sys_eth0_trans_colls":{"unit":None,"convert":None,"label":None},
            "sys_eth0_trans_carrier":{"unit":None,"convert":None,"label":None},
            "sys_eth0_trans_compressed":{"unit":None,"convert":None,"label":None},
            "sys_eth1_recv_bytes":{"unit":"KB","convert":_bytes_kb,"label":"Net eth1 recv"},
            "sys_eth1_recv_packets":{"unit":None,"convert":None,"label":None},
            "sys_eth1_recv_errs":{"unit":None,"convert":None,"label":None},
            "sys_eth1_recv_drop":{"unit":None,"convert":None,"label":None},
            "sys_eth1_recv_fifo":{"unit":None,"convert":None,"label":None},
            "sys_eth1_recv_frame":{"unit":None,"convert":None,"label":None},
            "sys_eth1_recv_compressed":{"unit":None,"convert":None,"label":None},
            "sys_eth1_recv_multicast":{"unit":None,"convert":None,"label":None},
            "sys_eth1_trans_bytes":{"unit":"KB","convert":_bytes_kb,"label":"Net eth1 trans"},
            "sys_eth1_trans_packets":{"unit":None,"convert":None,"label":None},
            "sys_eth1_trans_errs":{"unit":None,"convert":None,"label":None},
            "sys_eth1_trans_drop":{"unit":None,"convert":None,"label":None},
            "sys_eth1_trans_fifo":{"unit":None,"convert":None,"label":None},
            "sys_eth1_trans_colls":{"unit":None,"convert":None,"label":None},
            "sys_eth1_trans_carrier":{"unit":None,"convert":None,"label":None},
            "sys_eth1_trans_compressed":{"unit":None,"convert":None,"label":None},
            "sys_tun0_recv_bytes":{"unit":"KB","convert":_bytes_kb,"label":"Net tun0 recv"},
            "sys_tun0_recv_packets":{"unit":None,"convert":None,"label":None},
            "sys_tun0_recv_errs":{"unit":None,"convert":None,"label":None},
            "sys_tun0_recv_drop":{"unit":None,"convert":None,"label":None},
            "sys_tun0_recv_fifo":{"unit":None,"convert":None,"label":None},
            "sys_tun0_recv_frame":{"unit":None,"convert":None,"label":None},
            "sys_tun0_recv_compressed":{"unit":None,"convert":None,"label":None},
            "sys_tun0_recv_multicast":{"unit":None,"convert":None,"label":None},
            "sys_tun0_trans_bytes":{"unit":"KB","convert":_bytes_kb,"label":"Net tun0 trans"},
            "sys_tun0_trans_packets":{"unit":None,"convert":None,"label":None},
            "sys_tun0_trans_errs":{"unit":None,"convert":None,"label":None},
            "sys_tun0_trans_drop":{"unit":None,"convert":None,"label":None},
            "sys_tun0_trans_fifo":{"unit":None,"convert":None,"label":None},
            "sys_tun0_trans_colls":{"unit":None,"convert":None,"label":None},
            "sys_tun0_trans_carrier":{"unit":None,"convert":None,"label":None},
            "sys_tun0_trans_compressed":{"unit":None,"convert":None,"label":None},
            "mnesia_system_held_locks":{"unit":None,"convert":None,"label":"Mnesia Held Locks"},
            "mnesia_system_lock_queue":{"unit":None,"convert":None,"label":"Mnesia lock queue"},
            "mnesia_system_subscribers":{"unit":None,"convert":None,"label":"Mnesia subscribers"},
            "mnesia_system_tables":{"unit":None,"convert":None,"label":"Mnesia tables"},
            "mnesia_system_transactions":{"unit":None,"convert":None,"label":None},
            "mnesia_system_transaction_failures":{"unit":None,"convert":None,"label":None},
            "mnesia_system_transaction_commits":{"unit":None,"convert":None,"label":None},
            "mnesia_system_transaction_restarts":{"unit":None,"convert":None,"label":None},
            "mnesia_system_transaction_log_writes":{"unit":None,"convert":None,"label":None},
            "mnesia_table_voalte_caps_info_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_voalte_caps_info_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_voalte_caps_info_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_voalte_caps_info_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_pubsub_subscription_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_pubsub_subscription_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_pubsub_subscription_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_pubsub_subscription_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_roster_version_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_roster_version_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_roster_version_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_roster_version_size":{"unit":None,"convert":None,"label":None,"label":None},
            "mnesia_table_session_checkpoints":{"unit":None,"convert":None,"label":None,"label":None},
            "mnesia_table_session_subscribers":{"unit":None,"convert":None,"label":None,"label":None},
            "mnesia_table_session_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_session_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_irc_custom_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_irc_custom_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_irc_custom_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_irc_custom_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_pubsub_last_item_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_pubsub_last_item_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_pubsub_last_item_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_pubsub_last_item_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_pubsub_item_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_pubsub_item_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_pubsub_item_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_pubsub_item_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_muc_room_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_muc_room_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_muc_room_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_muc_room_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_muc_online_room_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_muc_online_room_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_muc_online_room_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_muc_online_room_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_acl_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_acl_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_acl_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_acl_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_privacy_checkpoints":{"unit":None,"convert":None,"label":None,"label":None},
            "mnesia_table_privacy_subscribers":{"unit":None,"convert":None,"label":None,"label":None},
            "mnesia_table_privacy_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_privacy_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_last_activity_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_last_activity_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_last_activity_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_last_activity_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_msg_delivery_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_msg_delivery_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_msg_delivery_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_msg_delivery_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_pubsub_index_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_pubsub_index_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_pubsub_index_memory":{"unit":None,"convert":None,"label":None,"label":None},
            "mnesia_table_pubsub_index_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_vcard_search_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_vcard_search_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_vcard_search_memory":{"unit":None,"convert":None,"label":None,"label":None},
            "mnesia_table_vcard_search_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_config_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_config_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_config_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_config_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_local_config_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_local_config_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_local_config_memory":{"unit":None,"convert":None,"label":None,"label":None},
            "mnesia_table_local_config_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_vp_config_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_vp_config_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_vp_config_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_vp_config_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_offline_msg_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_offline_msg_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_offline_msg_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_offline_msg_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_route_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_route_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_route_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_route_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_virtual_presence_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_virtual_presence_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_virtual_presence_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_virtual_presence_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_archive_message_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_archive_message_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_archive_message_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_archive_message_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_private_storage_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_private_storage_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_private_storage_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_private_storage_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_pubsub_state_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_pubsub_state_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_pubsub_state_memory":{"unit":None,"convert":None,"label":None,"label":None},
            "mnesia_table_pubsub_state_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_iq_response_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_iq_response_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_iq_response_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_iq_response_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_pubsub_node_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_pubsub_node_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_pubsub_node_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_pubsub_node_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_http_bind_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_http_bind_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_http_bind_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_http_bind_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_motd_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_motd_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_motd_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_motd_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_vcard_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_vcard_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_vcard_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_vcard_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_voalte_apns_id_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_voalte_apns_id_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_voalte_apns_id_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_voalte_apns_id_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_muc_registered_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_muc_registered_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_muc_registered_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_muc_registered_size":{"unit":None,"convert":None,"label":None,"label":None},
            "mnesia_table_archive_options_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_archive_options_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_archive_options_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_archive_options_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_s2s_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_s2s_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_s2s_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_s2s_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_voalte_offline_stats_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_voalte_offline_stats_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_voalte_offline_stats_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_voalte_offline_stats_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_caps_features_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_caps_features_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_caps_features_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_caps_features_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_motd_users_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_motd_users_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_motd_users_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_motd_users_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_voalte_stats_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_voalte_stats_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_voalte_stats_memory":{"unit":None,"convert":None,"label":None,"label":None},
            "mnesia_table_voalte_stats_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_roster_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_roster_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_roster_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_roster_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_sr_user_checkpoints":{"unit":None,"convert":None,"label":None,"label":None},
            "mnesia_table_sr_user_subscribers":{"unit":None,"convert":None,"label":None,"label":None},
            "mnesia_table_sr_user_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_sr_user_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_vs_counter_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_vs_counter_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_vs_counter_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_vs_counter_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_session_counter_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_session_counter_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_session_counter_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_session_counter_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_voalte_caps_ver_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_voalte_caps_ver_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_voalte_caps_ver_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_voalte_caps_ver_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_captcha_checkpoints":{"unit":None,"convert":None,"label":None,"label":None},
            "mnesia_table_captcha_subscribers":{"unit":None,"convert":None,"label":None,"label":None},
            "mnesia_table_captcha_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_captcha_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_schema_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_schema_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_schema_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_schema_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_voalte_offline_iq_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_voalte_offline_iq_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_voalte_offline_iq_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_voalte_offline_iq_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_vp_name_map_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_vp_name_map_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_vp_name_map_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_vp_name_map_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_sr_group_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_sr_group_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_sr_group_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_sr_group_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_register_ip_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_register_ip_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_register_ip_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_register_ip_size":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_vp_vocc_map_checkpoints":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_vp_vocc_map_subscribers":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_vp_vocc_map_memory":{"unit":None,"convert":None,"label":None},
            "mnesia_table_mod_vp_vocc_map_size":{"unit":None,"convert":None,"label":None},
            }
