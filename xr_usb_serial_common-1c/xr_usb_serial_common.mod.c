#include <linux/build-salt.h>
#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0x80c8b05d, "module_layout" },
	{ 0x634acce4, "usb_deregister" },
	{ 0x7c32d0f0, "printk" },
	{ 0x258b37db, "put_tty_driver" },
	{ 0x6232a5c4, "tty_unregister_driver" },
	{ 0x56287daf, "usb_register_driver" },
	{ 0x6f7163ff, "tty_register_driver" },
	{ 0x3f4094c8, "tty_set_operations" },
	{ 0x67b27ec1, "tty_std_termios" },
	{ 0x66b0e2c5, "__tty_alloc_driver" },
	{ 0xfd242dfd, "tty_port_register_device" },
	{ 0xc95316f5, "usb_get_intf" },
	{ 0x51e26df8, "usb_driver_claim_interface" },
	{ 0xd755c8f5, "_dev_info" },
	{ 0x12da5bb2, "__kmalloc" },
	{ 0x5a8371d5, "device_create_file" },
	{ 0x8263a5ba, "_dev_warn" },
	{ 0x4214105e, "usb_alloc_urb" },
	{ 0x8e856de9, "usb_alloc_coherent" },
	{ 0x6032570a, "tty_port_init" },
	{ 0xe346f67a, "__mutex_init" },
	{ 0xe91afbe9, "usb_ifnum_to_if" },
	{ 0xf4fa543b, "arm_copy_to_user" },
	{ 0xc6cbbc89, "capable" },
	{ 0x28cc25db, "arm_copy_from_user" },
	{ 0xbc10dd97, "__put_user_4" },
	{ 0x80fc0c5, "kmem_cache_alloc_trace" },
	{ 0xdf539367, "kmalloc_caches" },
	{ 0x5f754e5a, "memset" },
	{ 0x353e3fa5, "__get_user_4" },
	{ 0x71c90087, "memcmp" },
	{ 0x409873e3, "tty_termios_baud_rate" },
	{ 0x7bc77cd9, "tty_port_open" },
	{ 0xe707d823, "__aeabi_uidiv" },
	{ 0x524ccab1, "usb_autopm_put_interface" },
	{ 0x8027968f, "usb_autopm_get_interface" },
	{ 0xdb7305a1, "__stack_chk_fail" },
	{ 0x8f678b07, "__stack_chk_guard" },
	{ 0x55a910b8, "tty_standard_install" },
	{ 0xce90062e, "refcount_inc_not_zero_checked" },
	{ 0x97ab7daa, "tty_port_close" },
	{ 0xcef084ae, "usb_autopm_get_interface_async" },
	{ 0x5d638872, "tty_port_hangup" },
	{ 0xc4cec7a0, "tty_port_tty_wakeup" },
	{ 0x37a0cba, "kfree" },
	{ 0x2da7e1a5, "usb_put_intf" },
	{ 0xffb3c917, "tty_insert_flip_string_fixed_flag" },
	{ 0x74643ce6, "tty_flip_buffer_push" },
	{ 0x519df4d, "__tty_insert_flip_char" },
	{ 0xb2d48a2e, "queue_work_on" },
	{ 0x2d3385d3, "system_wq" },
	{ 0x91715312, "sprintf" },
	{ 0x25a5f9ee, "usb_driver_release_interface" },
	{ 0x9b0adf0d, "tty_port_put" },
	{ 0x92d97238, "usb_free_urb" },
	{ 0xa8aa8f4f, "tty_unregister_device" },
	{ 0x9a3ba060, "tty_kref_put" },
	{ 0x2ffc12ea, "tty_vhangup" },
	{ 0x4debd025, "tty_port_tty_get" },
	{ 0x67ea780, "mutex_unlock" },
	{ 0x52526626, "device_remove_file" },
	{ 0xc271c3be, "mutex_lock" },
	{ 0xc40ee47d, "usb_free_coherent" },
	{ 0xdb9ca3c5, "_raw_spin_lock" },
	{ 0x4205ad24, "cancel_work_sync" },
	{ 0xa5afa2f1, "usb_kill_urb" },
	{ 0x676bbc0f, "_set_bit" },
	{ 0x2a3aa678, "_test_and_clear_bit" },
	{ 0xd697e69a, "trace_hardirqs_on" },
	{ 0x2da81bff, "_raw_spin_lock_irq" },
	{ 0x6f4951e5, "usb_autopm_put_interface_async" },
	{ 0x6e6a6ecd, "tty_port_tty_hangup" },
	{ 0xa1633992, "_dev_err" },
	{ 0xa9217b9b, "usb_submit_urb" },
	{ 0x526c3a6c, "jiffies" },
	{ 0x9d669763, "memcpy" },
	{ 0x93b7b6b7, "dev_printk" },
	{ 0x9b884788, "usb_control_msg" },
	{ 0x2e5810c6, "__aeabi_unwind_cpp_pr1" },
	{ 0x39a12ca7, "_raw_spin_unlock_irqrestore" },
	{ 0x5f849a69, "_raw_spin_lock_irqsave" },
	{ 0xb1ad28e0, "__gnu_mcount_nc" },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=";

MODULE_ALIAS("usb:v04E2p1410d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v04E2p1411d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v04E2p1412d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v04E2p1414d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v04E2p1420d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v04E2p1421d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v04E2p1422d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v04E2p1424d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v04E2p1400d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v04E2p1401d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v04E2p1402d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v04E2p1403d*dc*dsc*dp*ic*isc*ip*in*");

MODULE_INFO(srcversion, "2139A7C0571EA98ADB704A8");
