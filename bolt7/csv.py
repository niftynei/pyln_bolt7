csv = [
    "msgtype,announcement_signatures,259",
    "msgdata,announcement_signatures,channel_id,channel_id,",
    "msgdata,announcement_signatures,short_channel_id,short_channel_id,",
    "msgdata,announcement_signatures,node_signature,signature,",
    "msgdata,announcement_signatures,bitcoin_signature,signature,",
    "msgtype,channel_announcement,256",
    "msgdata,channel_announcement,node_signature_1,signature,",
    "msgdata,channel_announcement,node_signature_2,signature,",
    "msgdata,channel_announcement,bitcoin_signature_1,signature,",
    "msgdata,channel_announcement,bitcoin_signature_2,signature,",
    "msgdata,channel_announcement,len,u16,",
    "msgdata,channel_announcement,features,byte,len",
    "msgdata,channel_announcement,chain_hash,chain_hash,",
    "msgdata,channel_announcement,short_channel_id,short_channel_id,",
    "msgdata,channel_announcement,node_id_1,point,",
    "msgdata,channel_announcement,node_id_2,point,",
    "msgdata,channel_announcement,bitcoin_key_1,point,",
    "msgdata,channel_announcement,bitcoin_key_2,point,",
    "msgtype,node_announcement,257",
    "msgdata,node_announcement,signature,signature,",
    "msgdata,node_announcement,flen,u16,",
    "msgdata,node_announcement,features,byte,flen",
    "msgdata,node_announcement,timestamp,u32,",
    "msgdata,node_announcement,node_id,point,",
    "msgdata,node_announcement,rgb_color,byte,3",
    "msgdata,node_announcement,alias,byte,32",
    "msgdata,node_announcement,addrlen,u16,",
    "msgdata,node_announcement,addresses,byte,addrlen",
    "msgtype,channel_update,258",
    "msgdata,channel_update,signature,signature,",
    "msgdata,channel_update,chain_hash,chain_hash,",
    "msgdata,channel_update,short_channel_id,short_channel_id,",
    "msgdata,channel_update,timestamp,u32,",
    "msgdata,channel_update,message_flags,byte,",
    "msgdata,channel_update,channel_flags,byte,",
    "msgdata,channel_update,cltv_expiry_delta,u16,",
    "msgdata,channel_update,htlc_minimum_msat,u64,",
    "msgdata,channel_update,fee_base_msat,u32,",
    "msgdata,channel_update,fee_proportional_millionths,u32,",
    "msgdata,channel_update,htlc_maximum_msat,u64,",
    "msgtype,query_short_channel_ids,261,gossip_queries",
    "msgdata,query_short_channel_ids,chain_hash,chain_hash,",
    "msgdata,query_short_channel_ids,len,u16,",
    "msgdata,query_short_channel_ids,encoded_short_ids,byte,len",
    "msgdata,query_short_channel_ids,tlvs,query_short_channel_ids_tlvs,",
    "tlvtype,query_short_channel_ids_tlvs,query_flags,1",
    "tlvdata,query_short_channel_ids_tlvs,query_flags,encoding_type,byte,",
    "tlvdata,query_short_channel_ids_tlvs,query_flags,encoded_query_flags,byte,...",
    "msgtype,reply_short_channel_ids_end,262,gossip_queries",
    "msgdata,reply_short_channel_ids_end,chain_hash,chain_hash,",
    "msgdata,reply_short_channel_ids_end,full_information,byte,",
    "msgtype,query_channel_range,263,gossip_queries",
    "msgdata,query_channel_range,chain_hash,chain_hash,",
    "msgdata,query_channel_range,first_blocknum,u32,",
    "msgdata,query_channel_range,number_of_blocks,u32,",
    "msgdata,query_channel_range,tlvs,query_channel_range_tlvs,",
    "tlvtype,query_channel_range_tlvs,query_option,1",
    "tlvdata,query_channel_range_tlvs,query_option,query_option_flags,bigsize,",
    "msgtype,reply_channel_range,264,gossip_queries",
    "msgdata,reply_channel_range,chain_hash,chain_hash,",
    "msgdata,reply_channel_range,first_blocknum,u32,",
    "msgdata,reply_channel_range,number_of_blocks,u32,",
    "msgdata,reply_channel_range,sync_complete,byte,",
    "msgdata,reply_channel_range,len,u16,",
    "msgdata,reply_channel_range,encoded_short_ids,byte,len",
    "msgdata,reply_channel_range,tlvs,reply_channel_range_tlvs,",
    "tlvtype,reply_channel_range_tlvs,timestamps_tlv,1",
    "tlvdata,reply_channel_range_tlvs,timestamps_tlv,encoding_type,byte,",
    "tlvdata,reply_channel_range_tlvs,timestamps_tlv,encoded_timestamps,byte,...",
    "tlvtype,reply_channel_range_tlvs,checksums_tlv,3",
    "tlvdata,reply_channel_range_tlvs,checksums_tlv,checksums,channel_update_checksums,...",
    "subtype,channel_update_timestamps",
    "subtypedata,channel_update_timestamps,timestamp_node_id_1,u32,",
    "subtypedata,channel_update_timestamps,timestamp_node_id_2,u32,",
    "subtype,channel_update_checksums",
    "subtypedata,channel_update_checksums,checksum_node_id_1,u32,",
    "subtypedata,channel_update_checksums,checksum_node_id_2,u32,",
    "msgtype,gossip_timestamp_filter,265,gossip_queries",
    "msgdata,gossip_timestamp_filter,chain_hash,chain_hash,",
    "msgdata,gossip_timestamp_filter,first_timestamp,u32,",
    "msgdata,gossip_timestamp_filter,timestamp_range,u32,",
]
